/**
 * Unpacking atoms by applying symmetry operators. Uses atom-atom collision
 * detection to remove duplicates.
 *
 * Compile with `gcc -shared -o unpack.so -fPIC -O3 unpack_v4.c`.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * Applies a symmetry operator to a location without using eval.
 */
float * applySymmetry(float location[3], char *symmetryOperator)
{
    int i = 0, op = 0, sign = 1;
    float total = 0;
    static float output[3];
    for (i = 0; i < strlen(symmetryOperator); i++)
    {
        switch(*(symmetryOperator + i))
        {
            case ',':
                while (total >= 1.0) { total -= 1.0; }
                while (total < 0.0) { total += 1.0; }
                output[op] = total;
                total = 0;
                sign = 1;
                op++;
                break;

            case '+':
                sign = 1;
                break;

            case '-':
                sign = -1;
                break;

            case '/':
                total += sign * atof(symmetryOperator + i - 1) / atof(symmetryOperator + i + 1);
                break;

            case 'x':
                total += location[0] * sign;
                break;

            case 'y':
                total += location[1] * sign;
                break;

            case 'z':
                total += location[2] * sign;
                break;
        }
    }
    while (total >= 1.0) { total -= 1.0; }
    while (total < 0.0) { total += 1.0; }
    output[op] = total;
    return output;
}
