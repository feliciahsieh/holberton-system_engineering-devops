#include <stdio.h>

int main()
{ /* Compile with gcc -o hello $CFILE -lncurses */
  /*  initscr();
  printw("cand that piece of art is useful\" - Dora Korpar, 2015-10-19 ");
  refresh();
  getch(); */

  write(1, "and that piece of art is useful\" - Dora Korpar, 2015-10-19\n",58); 

  return 1;
}
