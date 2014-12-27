This script detects any changes made to the rust files (`.rs`)
in current working directory and serves as an *autoloader* for your development.

Use this when you are learning rust/testing/editing rust files and
you're tired of doing `rustc test.rs` and `./test` over and over again.

Put this in the directory where your working rust files are and keep it running using something like `python autoloader.py`.

NOTE: This script is not meant to be any kind of substitute for `cargo build`.
Use this only when you're toying on some `.rs` files and don't use it in any serious project.
