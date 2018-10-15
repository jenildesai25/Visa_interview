// VISA Full time bachelor question.
class Result {

#     /*
#      * Complete the 'powerJump' function below.
#      *
#      * The function is expected to return an INTEGER.
#      * The function accepts STRING game as parameter.
#      */
#
     public static int powerJump(String game) {
     // Write your code here
     int count = 1;
     int step = Integer.MIN_VALUE;
     char ch = game.charAt(game.length() - 1);
     for (int i = 0; i < game.length(); i++) {
         if (game.charAt(i) == ch) {
             if (count > step) {
                 step = count;
             }
             count = 1;
         }
         else
             count++;
     }
     return step;
 }

 }