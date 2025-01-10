#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2) //checks the program usage
    {
        printf("correct usage is: ./recover image\n");
        return 1;
    }
    FILE *f = fopen(argv[1], "r");
    if (f == NULL)
    {
        printf("File is not there\n");
        return 2;
    }
    unsigned char buffer[512];
    int counter = 0;
    FILE *newFile = NULL;
    char *filename = malloc(8 * sizeof(char));
    while (fread(buffer, sizeof(char), 512, f))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            sprintf(filename, "%03i.jpg", counter);
            newFile = fopen(filename, "w");
            counter++;
        }
        if (newFile != NULL)
        {
            fwrite(buffer, sizeof(char), 512, newFile);
        }
    }
    free(filename);
    fclose(newFile);
    fclose(f);
    return 0;
}