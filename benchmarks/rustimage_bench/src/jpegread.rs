extern crate image;

use std::env;
use std::fs::File;
use std::io::BufReader;
use image::ImageDecoder;
use image::jpeg::JPEGDecoder;

fn load_jpeg(filename: &str) {
    let file = File::open(filename).unwrap();
    let buffered_reader = BufReader::new(file);
    let mut decoder = JPEGDecoder::new(buffered_reader);
    decoder.read_image().unwrap();
}

fn main() {
    let img = env::args().last().unwrap();
    for _ in (0..500) {
        load_jpeg(&img);
    }
}
