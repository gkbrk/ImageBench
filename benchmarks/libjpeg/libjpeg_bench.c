#include <stdio.h>
#include <stdlib.h>
#include <jpeglib.h>
#include <jerror.h>

int load_jpeg(char *fileName) {
    struct jpeg_decompress_struct info;
    struct jpeg_error_mgr err;
    
    FILE *file = fopen(fileName, "rb");

    info.err = jpeg_std_error(&err);
    jpeg_create_decompress(&info);

    if (!file) {
        printf("Error reading JPEG file\n");
        return 0;
    }

    jpeg_stdio_src(&info, file);
    jpeg_read_header(&info, TRUE);
    jpeg_start_decompress(&info);

    unsigned char *jdata = malloc(info.output_width * 3); // Data for a single row
    unsigned char *rowptr[1] = {jdata};
    while (info.output_scanline < info.output_height) {
        jpeg_read_scanlines(&info, rowptr, 1);
    }
    free(jdata);
    jpeg_finish_decompress(&info);
    fclose(file);
    return 0;
}

int main(int argc, char *argv[]) {
    for (int i=0;i<500;i++) {
        load_jpeg(argv[1]);
    }
    return 0;
}
