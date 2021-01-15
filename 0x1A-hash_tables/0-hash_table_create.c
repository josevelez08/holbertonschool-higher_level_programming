#include "hash_tables.h"
/**
 * hash_table_create - create a hash table
 * @size: size of the hash table
 * Return: A pointer of the hash table
 */
hash_table_t *hash_table_create(unsigned long int size)
{
		 hash_table_t *c;
		unsigned long int i = 0;

		c = malloc(sizeof(hash_node_t));
		if (c == NULL)
		{
			return (NULL);
		}

		c->size = size;
		c->array = malloc(sizeof(hash_node_t) * size);
		if (c->array == NULL)
		{
			free(c);
			return (NULL);
		}

		while (i < size)
		{
			c->array[i] = '\0';
			i++;
		}

		return (c);
}
