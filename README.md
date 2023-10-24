# esp-idf_rizzo

## how to use
1. Clone this repo
    ```
    git clone https://github.com/austinc3030/esp-idf_rizzo.git --recurse-submodules
    ```
2. Build and extract ghidra to `esp-idf_rizzo/ghidra`. Recommend using
    ```
    git clone --branch xtensa-support https://github.com/austinc3030/ghidra.git
    ```
5. Build signatures
    ```
    ./generate_all.py
    ```
and wait... for a while... like, days depending on your computer.
