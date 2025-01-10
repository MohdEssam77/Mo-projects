#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    if (strlen(argv[1]) != 26)
    {
        printf("key should be 26 alphabits.\n");
        return 1;
    }
    int score = 0;
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (islower(argv[1][i]))
        {
            score++;
        }
        if (isupper(argv[1][i]))
        {
            score++;
        }
    }
    if (score != 26)
    {
        printf("key should be 26 alphabits.\n");
        return 1;
    }
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        for (int j = 0; j < i; j++)
        {
            if (argv[1][i] == argv[1][j])
            {
                printf("key should be 26 different alphabits.\n");
                return 1;
            }
        }
    }
    string text = get_string("plaintext: ");
    int index;
    char new[strlen(text) + 1];
    for (int k = 0; k < strlen(text); k++)
    {
        if (isupper(text[k]))
        {
            index = text[k] - 65;
            new[k] = toupper(argv[1][index]);
        }
        else
        {
            if (islower(text[k]))
            {
                index = text[k] - 97;
                new[k] = tolower(argv[1][index]);
            }
            else
            {
                new[k] = text[k];
            }
        }
    }
    new[strlen(text)] = '\0';
    printf("ciphertext: %s\n", new);
}
