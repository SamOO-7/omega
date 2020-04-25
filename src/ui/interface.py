#!/usr/bin/env python3

#            ---------------------------------------------------
#                              Omega Framework                                
#            ---------------------------------------------------
#                  Copyright (C) <2020>  <Entynetproject>       
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        any later version.
#
#        This program is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#        GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Omega shell interface

Handles general behavior of Omega interactive command-line interface.
"""
# pylint: disable=too-many-lines
# pylint: disable=too-many-public-methods
__all__ = ["Shell"]

import os
import traceback
import shnake

import core
from core import session, tunnel, plugins, encoding
import datatypes
from datatypes import Path
import ui.output
from ui.color import colorize
import ui.input
import utils.path

READLINE_COMPLETER_DELIMS = ' \t\n`~!#$%^&*()=+[{]}\\|;:\'",<>?'


class Shell(shnake.Shell):
    """Omega shell interface"""

    prompt = colorize('%Lined', 'omega', '%Reset', '> ')

    _nocmd = "[-] Unrecognized command!"
    nohelp = "[-] No help for %s!"
    error = "[-] %s!"

    bind_command = None

    def __init__(self):
        self.nocmd = None
        self.last_exception = None
        super().__init__()
        try:
            import readline
            readline.set_history_length(session.Hist.MAX_SIZE)
            readline.set_completer_delims(READLINE_COMPLETER_DELIMS)
        except ImportError:
            pass

    def init(self):
        """Omega interface init"""
        # load Omega plugins list
        plugins.blacklist = self.get_names(self, "do_")
        plugins.reload(verbose=False)

    # pylint: disable=arguments-differ
    def precmd(self, argv):
        """Handle pre command hooks such as session aliases"""
        # Make 'nocmd' error message explicit if tunnel is connected
        self.nocmd = self._nocmd
        if tunnel:
            import time
            time.sleep(0)
        # Reset backlog before each command except backlog
        if self.bind_command:
            if len(argv) == 1 and argv[0] == "exit":
                # self.bind_command = None
                pass
            else:
                argv.insert(0, self.bind_command)
        if argv and argv[0] != "backlog":
            self.stdout.backlog = ""
        # Alias Handler
        try:
            cmds = self.parseline(session.Alias[argv[0]])
        except (KeyError, IndexError):
            return argv
        self.interpret(cmds[:-1], precmd=(lambda x: x))
        return cmds[-1] + argv[1:]

    def onecmd(self, argv):
        if "id" in session.Compat and session.Compat["id"] == "v1":
            print("[!] Warning: You are using a v1-compatible session file")
            print("[!]          please upgrade $TARGET with new $PAYLOAD")
            print("[!]          and run `session upgrade` when done.")
            print("")
        print("[v] %s: Running..." % self.debug_cmdrepr(argv))
        return super().onecmd(argv)

    def postcmd(self, retval, argv):
        """Post command hook

        Redraw shell prompt
        """
        int_retval = self.return_errcode(retval)
        print("[v] %s: Returned %d" % (self.debug_cmdrepr(argv), int_retval))
        # redraw shell prompt after each command
        prompt_elems = ["%Lined", "omega"]
        if tunnel:
            # if remote shell, add target hostname to prompt
            prompt_elems += ["%Reset", "(", "%BoldRed",
                             tunnel.hostname, "%Reset", ")"]
        if self.bind_command:
            # If a command is binded to the prompt
            prompt_elems += ["%ResetBoldWhite", " #", self.bind_command]
        prompt_elems += ["%Reset", "> "]
        self.prompt = colorize(*prompt_elems)

        return retval

    def completenames(self, text, line, *_):
        """Add aliases and plugins for completion"""
        argv = line.split()
        if (len(argv) == 2 and line and line[-1] == " ") or len(argv) > 2:
            return []
        result = super().completenames(text, line, *_)
        result += list(session.Alias)
        if tunnel:
            result += list(plugins)
        return [x for x in list(set(result)) if x.startswith(text)]

    def onexception(self, exception):
        """Add traceback handler to onexception"""
        exc = traceback.format_exception(type(exception),
                                         exception,
                                         exception.__traceback__)
        # a small patch for traceback from plugins, remove trash lines
        for idx, line in enumerate(exc):
            if ('File "<frozen importlib._bootstrap>"' in line
                    and '_call_with_frames_removed' in line):
                exc = exc[(idx + 1):]
                header = "Traceback (most recent call last):"
                exc.insert(0, header + os.linesep)
                break
        self.last_exception = "".join(exc).splitlines()
        for line in self.last_exception:
            print(colorize("[v] ", "%Red", line))
        return super().onexception(exception)

    def default(self, argv):
        """Fallback to plugin command (if any)"""
        if argv[0] in plugins.keys():
            if tunnel:
                return plugins.run(argv)
        return super().default(argv)

    #################
    # COMMAND: exit #
    @staticmethod
    
    def do_disconnect(argv):
        """Disconnect target server."""
        if tunnel:
            tunnel.close()
            return True
        else:
            print("[-] Target server is not connected!")

    def do_exit(argv):
        """Exit Omega Framework."""
        if tunnel:
            tunnel.close()
        exit()

    ####################
    # COMMAND: connect #
    @staticmethod
    def complete_connect(text, line, *_):
        """autocompletion for `connect` command"""
        argv = line.split()
        if (len(argv) == 2 and line[-1] == " ") or len(argv) > 2:
            return []
        keys = ["--get-payload"]
        return [x for x in keys if x.startswith(text)]

    def do_run(self, argv):
        """Connect target server.

        USAGE:
            connect

        DESCRIPTION:
            Connect to remote target URL (`help set TARGET`).

            If payload (`connect --get-payload`) is correctly
            injected in target URL, Omega spawns a remote shell.

        OPTIONS:
            --get-payload
                Display current payload code, as it should be
                injected on target URL.
        """
        obj = str(session.Conf.PAYLOAD(call=False))
        obj = obj.replace("%%PASSKEY%%", session.Conf.PASSKEY().upper())

        if len(argv) > 1:
            if argv[1] == "--get-payload":
                print(obj)
                return True
            self.interpret("help connect")
            return False

        print("[*] Current payload is: " + obj + "\n")

        if tunnel:
            m = ("[*] Use `set TARGET <value>` to use another url as target."
                 "\n[*] To connect a new server, disconnect from «{}» first.")
            print(m.format(session.Env.HOST))
            return False

        if session.Conf.TARGET() is None:
            m = ("To run a remote tunnel, the payload shown above must be\n"
                 "manually injected in a remote server executable web page.\n"
                 "Then, use `set TARGET <payloaded_url>` and run `run`.")
            print(colorize("%BoldCyan", m))
            return False

        return tunnel.open()  # it raises exception if fails
    
    @staticmethod
    # pylint: disable=unused-argument
    def do_update(argv):
        """Update Omega Framework."""
        import os
        os.system("chmod +x etc/update.sh && etc/update.sh")
    
    ################
    # COMMAND: set #
    @staticmethod
    def complete_set(text, line, *_):
        """Use settings as `set` completers (case insensitive)"""
        argv = line.split()
        if (len(argv) == 2 and line[-1] == " ") or len(argv) > 2:
            return []
        result = []
        for key in session.Conf.keys():
            if key.startswith(text.upper()):
                result.append(key)
        return result

    @staticmethod
    def do_pymode(argv):
        """Run Omega Framework python mode."""
        from ui import console
        console = console.Console()
        return console()

    @staticmethod
    def do_clear(argv):
        """Clear terminal window."""
        import os
        os.system("clear")
    
    @staticmethod
    def do_info(argv):
        """Show configuration settings."""
        string = (argv + [""])[1]
        print(session.Conf(string))

    @staticmethod
    def do_set(argv):
        """Edit configuration settings.

        USAGE:
            set <variable> <value>

        DESCRIPTION:
            Settings are a collection of editable variables that affect
            Omega core behavior.
            - Their value is bound to current session.
            - To permanently change a setting's value at start, it
            must be defined by hand on Omega config file.

            > set
              - Display current settings

            > set <string>
              - Display settings whose name starts with string

            > set <variable> <value>
              - Assign VALUE to VAR setting (only if it's a valid value)

            > set <variable> %%DEFAULT%%
              - Reset VAR's default value with '%%DEFAULT%%' magic string

            > set <variable> "file:///path/to/file"
              - Bind VAR's value to a local file content

            > set <variable> +
              - Open VAR's value in text editor. This is useful to edit
              values with multiple lines

            > set <variable> + <line>
              - Add line to the end of variable's value

            > set <variable> + "file:///path/to/file"
              - Re-bind VAR to a local file path.
              Even if path doesn't exist, the setting will take the value of
              the file if it founds it. Otherwise, previous buffer value is
              kept as long as the file path is unreachable

        Defining HTTP Headers:
            You can define custom http request header fields by hand.

            Settings starting with 'HTTP_' are automagically treated as
            HTTP Request Headers values.

            By default, only the "User-Agent" Header is defined. It is bound
            by default to a local file containing common HTTP User Agents.
            (`help set HTTP_USER_AGENT`)

            * Examples:
            > set HTTP_ACCEPT_LANGUAGE "en-CA"
              - Define "Accept-Language" http request header field.
            > set HTTP_ACCEPT_LANGUAGE None
              - Remove HTTP_ACCEPT_LANGUAGE header with magic value 'None'.

        Use `set help <variable>` for detailed help about a setting.
        """
        # `set [<STRING>]` display concerned settings list
        if len(argv) < 3:
            try:
                if string not in session.Conf:
                    string = "<variable>"
                print("[*] For detailed help, run `help set %s`." % string)
            except:
                string = "<variable>"
                print("[*] For detailed help, run `help set %s`." % string)

        # buffer edit mode
        elif argv[2] == "+":
            # `set <variable> +`: use $EDITOR as buffer viewer in file mode
            if len(argv) == 3:
                # get a buffer obj from setting's raw buffer value
                file_name = argv[1].upper()
                file_ext = "txt"
                setting_obj = session.Conf[argv[1]](call=False)
                if isinstance(setting_obj, datatypes.PhpCode):
                    file_ext = "php"
                elif isinstance(setting_obj, datatypes.ShellCmd):
                    file_ext = "sh"
                buffer = Path(filename="%s.%s" % (file_name, file_ext))
                buffer.write(session.Conf[argv[1]].buffer)
                # try to edit it through $EDITOR, and update it
                # if it has been modified.
                if buffer.edit():
                    session.Conf[argv[1]] = buffer.read()
            # `set <variable> + "value"`: add value on setting possible choices
            else:
                session.Conf[argv[1]] += " ".join(argv[3:])
        # `set <variable> "value"`: just change VAR's "value"
        else:
            session.Conf[argv[1]] = " ".join(argv[2:])

    ################
    # COMMAND: env #
    @staticmethod
    def complete_env(text, line, *_):
        """Use env vars as `env` completers (case insensitive)"""
        argv = line.split()
        if (len(argv) == 2 and line[-1] == " ") or len(argv) > 2:
            return []
        result = []
        for key in session.Env:
            if key.startswith(text.upper()):
                result.append(key)
        return result

    @staticmethod
    def do_env(argv):
        """Show environment variables.

        USAGE:
            env <name> <value>

        DESCRIPTION:
            Environment variables are meant to store informations
            about remote server state.
            - Their initial value is defined as soon as Omega
            opens a remote connection (`run`).
            - Plugins can read, write, and create environment variables.

            > env
            - Display all current env vars

            > env <string>
            - Display all env vars whose name starts with STRING.

            > env <name> <value>
            - Set name env variable's value to value.

            > env <name> None
            - Remove name with 'None' magic string.

        EXAMPLE:
            `PWD` is used to persist 'current working directory' of remote
            target. It allows plugins to use relative path arguments:
            # set PWD to '/var/www':
            > cd /var/www
            # display '/var/www/index.php':
            > cat index.php`

        NOTES:
            - Some envionment variables, such as `PWD` and `WEB_ROOT` are
            crucial for remote session consistency. Be careful before
            manually editing them.

            - Plugins that need to store persistent informations may and
            must use env vars. For example, the `mysql` plugin creates a
            `MYSQL_CRED` environment variable, which contains remote
            database connection credentials. So next calls to `mysql` can be
            used to browse database without providing credentials each time.

            - Unlike Settings (`set` command), env vars are meant to store
            basic strings.
        """
        # `env [<NAME>]`
        if len(argv) < 3:
            if not session.Env:
                print("[!] Must connect to spread env vars.")
                return False
            print(session.Env((argv + [""])[1]))
            return True
        # `env <NAME> <value>`
        session.Env[argv[1]] = " ".join(argv[2:])
        return True

    ##################
    # COMMAND: bind #
    def complete_bind(self, text, line, *_):
        """autocompletion for `bind` command"""
        result = self.completenames(text, line, *_)
        if not result:
            return []
        result = [x for x in result if x != "bind"]
        if tunnel:
            result += plugins.keys()
        return [x for x in list(set(result)) if x.startswith(text)]

    def do_bind(self, argv):
        """Attach a command to prompt.

        USAGE:
            bind <command>

        DESCRIPTION:
            Bind Omega prompt to command.
            Every line executed will then be executed as if it was
            the arguments of COMMAND.
            This is useful for plugins like `run` or `mysql`, when you
            are working from them and don't want to re-type the plugin
            name again and again ..

            NOTE: press Ctrl-D or type exit to 'unbind' from current command.

        DEMO:
            omega(ehtools.pro)>> run type ls
            ls is /bin/ls
            omega(ehtools.pro)>> type ls
            [-] Unrecognized Command: type
            omega(ehtools.pro)>> bind run
            [!] Type exit to leave binded 'run' subshell.
            # now shell is bound to `run`, so we just need to execute `type ls`
            omega(ehtools.pro)> #run> type ls
            ls is /bin/ls
        """
        if len(argv) != 2 or argv[1] not in self.complete_bind("", ""):
            self.interpret("help bind")
        else:
            self.bind_command = argv[1]


    #################
    # COMMAND: help #
    def complete_help(self, text, line, *_):
        """Use settings as `set` completers (case insensitive)"""
        argv = line.split()
        if argv[:2] == ["help", "set"]:
            if (len(argv) == 2 and line[-1] == " ") \
                    or (len(argv) == 3 and line[-1] != " "):
                return [x for x in session.Conf if x.startswith(text)]
            if len(argv) > 2 or line[-1] == " ":
                return []
        return self.completenames(text, line, *_)

    def do_help(self, argv):
        """Show help information.

        USAGE:
            help
            help <command>
            help set <variable>

        DESCRIPTION:
            Get help for any core command or plugin.

            If called without arguments, a list of available commands,
            plugins, and aliases is displayed.
            Otherwise, detailed help of given command is shown.

            * NOTE: plugins are only listed after running `run`

        EXAMPLES:
            > help
              - List available commands, plugins, and aliases
            > help help
              - Get detailed help on `help` command
            > help exit
              - Display the help for the `exit` command
            > help set PAYLOAD
              - Display help about the "PAYLOAD" setting
        """
        def get_doc(cmd):
            """get lines from `cmd` docstring"""
            doc = ""
            if hasattr(self, "do_" + cmd):
                doc = getattr(self, "do_" + cmd).__doc__
            elif cmd in plugins:
                doc = plugins[cmd].help
                if doc.strip():
                    doc += "\nPLUGIN LOCATION:\n    " + plugins[cmd].path
            return doc.strip().splitlines()

        def get_description(doc_lines):
            """get formatted command help description"""
            if doc_lines:
                return doc_lines[0].strip()
            return colorize("%Yellow", "No description")

        def doc_help(doc_lines):
            """print formated command's docstring"""
            # reject empty docstrings (description + empty line)
            if len(doc_lines) < 2:
                return False
            doc_lines.pop(0)  # remove the description line
            while not doc_lines[0].strip():
                doc_lines.pop(0)  # remove heading empty lines
            # remove junk leading spaces (due to python indentation)
            trash = len(doc_lines[0]) - len(doc_lines[0].lstrip())
            doc_lines = [line[trash:].rstrip() for line in doc_lines]
            # hilight lines with no leading spaces (man style)
            result = ""
            for line in doc_lines:
                if line == line.lstrip():
                    line = colorize("%BoldWhite", line)
                elif line.startswith("    * "):
                    line = colorize("    * ", "%Yellow", line[6:])
                elif line.startswith("    > "):
                    line = colorize("    > ", "%Cyan", line[6:])
                elif line.startswith("    # "):
                    line = colorize("%Dim", line)
                elif line.startswith("    -") and line[5] != " ":
                    line = colorize("%Green", line)
                result += line + "\n"
            print(result)
            return True

        # help set <variable>
        if len(argv) >= 3 and argv[1] == "set":
            var = argv[2].upper()
            try:
                doc = getattr(session.Conf, var).docstring
            except KeyError:
                print("[-] %s: No such variable!" \
                        % var)
                return False
            print("\n[*] Help for %s variable:\n" % var)
            return doc_help(doc.splitlines())

        # help <COMMAND>
        if len(argv) >= 2:
            doc = get_doc(argv[1])
            if doc:
                print("\n[*] %s: %s\n" % (argv[1], get_description(doc)))
                # call help_COMMAND() or fallback to COMMAND's docstring
                help_method = getattr(self, "help_" + argv[1], None)
                if callable(help_method):
                    getattr(self, 'help_' + argv[1])()
                else:
                    if not doc_help(doc):
                        return False
                if argv[1] in session.Alias:
                    print("[!] Warning: %r has been aliased."
                          % (argv[1], argv[1]))
                return True
            # fallback to alias display
            elif argv[1] in session.Alias:
                return self.interpret("alias %s" % argv[1])
            print(self.nohelp % argv[1])
            return False

        # help
        core_commands = self.get_names(self, "do_")
        full_help = [('\nCore Commands', core_commands)]
        max_len = max(13, len(max(core_commands, key=len)))
        print("")
        os.system("cat data/cmds/core_commands.list")
        print("")
        if tunnel:
                os.system("cat data/cmds/commands.list")
                print("")

    # pylint: disable=invalid-name
    @staticmethod
    def except_OSError(exception):
        """Fix OSError args, removing errno, and adding filename"""
        if isinstance(exception.errno, int):
            exception.args = (exception.strerror,)
        if exception.filename is not None:
            exception.args += ("«{}»".format(exception.filename),)
        return exception

    @staticmethod
    def debug_cmdrepr(argv):
        """Returns a nice representation of given command arguments
        """
        cmdrepr = []
        for arg in argv:
            if not isinstance(arg, str):
                continue
            argrepr = repr(arg)
            sep = argrepr[0], argrepr[-1]
            argrepr = argrepr[1:-1].join(colorize("%DimCyan", "%Reset"))
            cmdrepr.append(sep[0] + argrepr + sep[1])
        args = " ".join(cmdrepr)
        return colorize("%BoldCyan", "CMD(", "%Reset", args, "%BoldCyan", ")")
