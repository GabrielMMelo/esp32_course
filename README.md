# Curso de ESP32
[![License: CC BY-ND 4.0](https://img.shields.io/badge/License-CC%20BY--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nd/4.0/)

Curso introdutório da utilização do dispositivo utilizando [MicroPython](https://micropython.org/).

## Instalação da toolchain

1- Adicione o seguinte trecho ao final do arquivo `~/.bashrc`

``` bash
    export PATH=$PATH:$HOME/esp/xtensa-esp32-elf/bin
    alias get_esp32="export PATH=$PATH:$HOME/esp/xtensa-esp32-elf/bin"
    export IDF_PATH=~/esp/esp-idf
```

2- Instale as dependências

``` bash
    sudo apt-get install git wget make libncurses-dev flex bison gperf python python-serial
```

3- Baixe a toolchain

``` bash
    mkdir ~/esp && cd ~/esp
    wget -c https://dl.espressif.com/dl/xtensa-esp32-elf-linux64-1.22.0-61-gab8375a-5.2.0.tar.gz
    tar zxvf xtensa-esp32-elf-linux64-1.22.0-61-gab8375a-5.2.0.tar.gz
```

## Instalação da API ESP-IDF

4- Baixe a API. O `--recursive` garantirá que os submódulos do repositório, que são essenciais para compilação, também sejam baixados

``` bash
    git clone --recursive https://github.com/espressif/esp-idf.git
```

### Hello World

5- Copie o exemplo `Hello World` para a pasta atual
```bash
    cp -r ~/esp/esp-idf/examples/get-started/hello_world/ .
``` 

6- Entre na pasta e execute o menu de configurações
```bash
    cd hello_world && make menuconfig
```

__Antes de executar o__ `make` __, tenha certeza de que possui as permissões necessárias no diretório__ `esp-idf`
```bash
    sudo chmod -R 777 ~/.esp/esp-idf/
```

7- Após configurar o firmware com `menuconfig`, suba-o para o `esp32`
```bash
    make flash ESPPORT=/dev/tty{nome_da_porta_com}
```

8- Você pode conferir a saída do `esp32`
``` bash
    make monitor ESPPORT=/dev/tty{nome_da_porta_com}
```

Tudo certo até aqui? Prossiga para a instalação do `micropython`

## Instalando o Micropython

9- Tenha certeza de que você está no diretório `esp-idf/` e baixe o micropython
```bash
    git clone https://github.com/micropython/micropython-esp32.git
```

### Compilando port do esp32
10- Entre no diretório baixado e compile o mpy-cross
```bash
    make -C mpy-cross
```

11- Entre em `ports/esp32` e abra o `Makefile`
```bash
    cd ports/esp32 && vim Makefile
```

12- Abaixo da linha **24** ("# paths to ESP IDF and its components") inclua
```bash
   ESPIDF ?= $(HOME)/esp/esp-idf
```

13- Ainda no arquivo `Makefile` copie a hash armazenada em `ESPIDF_SUPHASH`


14- Volte ao diretório `esp-idf` e altere para o commit compatível com o `ESPIDF` baixado
```bash
    git checkout <hash_copiado_no_passo_anterior>
```

15- Entre no diretório `micropython-esp32` e atualize os submódulos
```bash
    git submodule update --init
```

16- Entre novamente no `ports/esp32` e execute
```bash
    make clean 
    make
```

17- Caso a compilação falhe, volte no diretório `esp-idf` e atualize os submódulos
```bash
    git submodule update --init --force
```

18- Ainda no diretório `ports/esp32`, apague o conteúdo da flash do `esp32` e suba o firmware
```bash
    make erase && make deploy
```

### Compilando port para Unix
O `Micropython` também pode ser executado em ambientes Unix, como o Linux. Essa pode ser uma boa estratégia para realização de testes e conferências, antes de realizar o deploy para o `esp32`.

19- Compile a port do unix
```bash
    cd ports/unix
    make
```

20- O `Micropython` pode ser acedido através de:
```
    ./micropython
```

#### `upip`, a versão do `pip` no `Micropython`
O `upip` é o gerenciador de pacotes do `Micropython` e pode ser útil para realizar o download de módulos do mesmo.

21- Para fazer o download do módulo `machine`, por exemplo:
```bash
    ./micropython -m upip install micropython-machine
```


## mpfshell

Para utilizar o terminal [mpfshell](https://github.com/wendlers/mpfshell) para upload/download de arquivos no `esp32`, utilize o mesmo procedimento adotado no meu [Guia de utilização do micropython para esp8266](https://github.com/GabrielMMelo/esp8266_course#mpfshell)


## EXTRA 
### Fork do micropython com suporte ao uasyncio 2.0 (pfalcon) 

Clone o repositório dentro de `esp-idf`
```bash
    git clone https://github.com/pfalcon/micropython
``` 

Insira o seguinte alias em seu `~/.bashrc`
```bash
    alias xtensa-esp32-elf-gcc="xtensa-esp32-elf"
```

**Os demais passos serão os mesmos do repositório oficial**


#### Links úteis
- [Guia de programação do ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/latest/) (Espressif IoT development framework)
- [Getting started do ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/latest/get-started/)
- [Toolchain no Linux](https://docs.espressif.com/projects/esp-idf/en/latest/get-started/linux-setup.html)
- [Getting started Micropython com ESP32](http://docs.micropython.org/en/latest/esp32/tutorial/intro.html#esp32-intro)
