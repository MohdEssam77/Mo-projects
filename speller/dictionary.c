// Implements a dictionary's functionality
#include <strings.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;
unsigned int counter;
unsigned int hashed;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    hashed = hash(word);
    node *val = table[hashed];
    while (val != 0)
    {
        if (strcasecmp(word, val->word) == 0)
        {
            return true;
        }
        val = val->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int total = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        total = total + tolower(word[i]);
    }
    int returned_value = total % N; //N here is 26 so we r finding the reminder after dividing the total by 26
    return returned_value;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *f = fopen(dictionary, "r");
    if (f == NULL)
    {
        printf("cannot open %s file\n", dictionary);
        return false;
    }
    char word[LENGTH + 1];
    while (fscanf(f, "%s", word) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        strcpy(n->word, word);
        hashed = hash(word);
        n->next = table[hashed];
        table[hashed] = n;
        counter++;
    }
    fclose(f);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    if (counter > 0)
    {
        return counter;
    }
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int j = 0; j < N; j++)
    {
        node *n = table[j];
        while (n != NULL)
        {
            node *n2 = n;
            n = n->next;
            free(n2);
        }
        if (n == NULL)
        {
            return true;
        }
    }
    return false;
}
