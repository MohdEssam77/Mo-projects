#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);
    double l = (letters * 100) / words;
    double s = (sentences * 100) / words;
    int x = 0.0588 * l - 0.296 * s - 15.8;
    printf("%i\n", letters);
    printf("%i\n", words);
    printf("%i\n", sentences);
    printf("%f\n", l);
    printf("%f\n", s);
    printf("%i\n", x);
    if (x > 16)
    {
        printf("Grade 16+\n");
    }
    if (x < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", x);
    }
}

int count_letters(string text)
{
    int lower = 0;
    int upper = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (islower(text[i]))
        {
            lower++;
        }
        if (isupper(text[i]))
        {
            upper++;
        }
    }
    return upper + lower;
}

int count_words(string text)
{
    int spaces = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == 32)
        {
            spaces++;
        }
    }
    return spaces + 1;
}

int count_sentences(string text)
{
    int end = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == 33 || text[i] == 46 || text[i] == 63)
        {
            end++;
        }
    }
    return end;
}