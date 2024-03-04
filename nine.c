#include <stdio.h>

#define MAX_SIZE 1000

int main() {
    FILE *file1, *file2, *merge_file;
    char file1_name[MAX_SIZE], file2_name[MAX_SIZE], merge_file_name[MAX_SIZE];
    char ch;
    printf("Enter the name of the first file: ");
    scanf("%s", file1_name);
    printf("Enter the name of the second file: ");
    scanf("%s", file2_name);
    printf("Enter the name of the new file to merge the above two files: ");
    scanf("%s", merge_file_name);


    file1 = fopen(file1_name, "r");
    if (file1 == NULL) {
        printf("Error: Unable to open the first file.\n");
        return 1;
    }


    file2 = fopen(file2_name, "r");
    if (file2 == NULL) {
        printf("Error: Unable to open the second file.\n");
        fclose(file1);
        return 1;
    }


    merge_file = fopen(merge_file_name, "w");
    if (merge_file == NULL) {
        printf("Error: Unable to create the merge file.\n");
        fclose(file1);
        fclose(file2);
        return 1;
    }

    
    while ((ch = fgetc(file1)) != EOF) {
        fputc(ch, merge_file);
    }
    while ((ch = fgetc(file2)) != EOF) {
        fputc(ch, merge_file);
    }

    printf("The contents of '%s' and '%s' have been successfully merged into '%s'.\n", file1_name, file2_name, merge_file_name);

    fclose(file1);
    fclose(file2);
    fclose(merge_file);

    return 0;
}
