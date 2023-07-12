// https://ir0nstone.gitbook.io/notes/types/stack/canaries

#include <cstdio>
#include <iostream>
#include <stdio.h>

void vuln()
{
	char buffer[64];
	memset(buffer, 'A', sizeof(buffer));

	printf("Addr: %p\n", buffer);
	fflush(stdout);

	printf("Leak me\n");
	fflush(stdout);
	fgets(buffer, 2048, stdin);

	printf(buffer);
	printf("");
	fflush(stdout);

	printf("Overflow me\n");
	fflush(stdout);
	fgets(buffer, 2048, stdin);

}

void win()
{
	puts("You won!");
	fflush(stdout);

}

int main()
{
	vuln();
}
