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

Baixe a API. O `--recursive` garantirá que os submódulos do repositório, que são essenciais para compilação, também sejam baixados

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

Está funcionando? Prossiga para a instalação do `micropython`

# Instalando o Micropython

Tenha certeza de que você está no diretório `esp-idf/` e baixe o micropython
```bash
    git clone https://github.com/micropython/micropython-esp32.git
```

Entre no diretório baixado e compile o mpy-cross
```bash
    make -C mpy-cross
```

Entre em `ports/esp32` e abra o `Makefile`
```bash
    cd ports/esp32 && vim Makefile
```

Abaixo da linha **24** ("# paths to ESP IDF and its components") inclua
```bash
   ESPIDF ?= $(HOME)/esp/esp-idf
```

Ainda no arquivo `Makefile` copie a hash armazenada em `ESPIDF_SUPHASH`


Volte ao diretório `esp-idf` e altere para o commit compatível com o `ESPIDF` baixado
```bash
    git checkout <hash_copiado_no_passo_anterior>
```

Entre no diretório `micropython-esp32` e atualize os submódulos
```bash
    git submodule update --init
```

Entre novamente no `ports/esp32` e execute
```bash
    make clean 
    make
```

Caso a compilação falhe, volte no diretório `esp-idf` e atualize os submódulos
```bash
    git submodule update --init --force
```

Ainda no diretório `ports/esp32`, apague o conteúdo da flash do `esp32` e suba o firmware
```bash
    make erase && make deploy
```

# mpfshell

Para utilizar o terminal [mpfshell](https://github.com/wendlers/mpfshell) para upload/download de arquivos no `esp32`, utilize o mesmo procedimento adotado no meu [Guia de utilização do micropython para esp8266](https://github.com/GabrielMMelo/esp8266_course#mpfshell)


# EXTRA 
## Fork do micropython com suporte ao uasyncio 2.0 (pfalcon) 

Clone o repositório dentro de `esp-idf`
```bash
    git clone https://github.com/pfalcon/micropython
``` 

Insira o seguinte alias em seu `~/.bashrc`
```bash
    alias xtensa-esp32-elf-gcc="xtensa-esp32-elf"
```

**Os demais passos serão os mesmos do repositório oficial**


### Links úteis
[Guia de programação do ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/latest/) (Espressif IoT development framework)
[Getting started do ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/latest/get-started/)
[Toolchain no Linux](https://docs.espressif.com/projects/esp-idf/en/latest/get-started/linux-setup.html)
