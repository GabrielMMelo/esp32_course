# Instalação da toolchain

Adicione no `~/.bashrc`

``` bash
    export PATH=$PATH:$HOME/esp/xtensa-esp32-elf/bin
    alias get_esp32="export PATH=$PATH:$HOME/esp/xtensa-esp32-elf/bin"
    export IDF_PATH=~/esp/esp-idf
```

Instale as dependências

``` bash
    sudo apt-get install git wget make libncurses-dev flex bison gperf python python-serial
```

Baixe a toolchain

``` bash
    mkdir ~/esp && cd ~/esp
    wget -c https://dl.espressif.com/dl/xtensa-esp32-elf-linux64-1.22.0-61-gab8375a-5.2.0.tar.gz
    tar zxvf xtensa-esp32-elf-linux64-1.22.0-61-gab8375a-5.2.0.tar.gz
```

# Instalação da API ESP-IDF

Baixe a API. O `--recursive` garantirá que os submódulos do repositórios, que são essenciais para compilação, também sejam baixados

``` bash
    git clone --recursive https://github.com/espressif/esp-idf.git
```

## Hello World

Copie o exemplo `Hello World` para a pasta atual
```bash
    cp -r ~/esp/esp-idf/examples/get-started/hello_world/ .
``` 

Entre na pasta e execute o menu de configurações
```bash
    cd hello_world && make menuconfig
```

__Antes de executar o__ `make` __, tenha certeza de que possui as permissões necessárias no diretório__ `esp-idf`
```bash
    sudo chmod -R 777 ~/.esp/esp-idf/
```

Após configurar o firmware com `menuconfig`, suba-o para o `esp32`
```bash
    make flash ESPPORT=/dev/tty{nome_da_porta_com}
```

Você pode conferir a saída do `esp32`
``` bash
    make monitor ESPPORT=/dev/tty{nome_da_porta_com}
```

