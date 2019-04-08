{% args req %}
<html lang="pt">
    <head>
        <style rel="stylesheet" type="text/css">
            body{
                background-color: #680068;
                font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
            }
            .container {
                width: 50%;
                margin: 0 auto;
                margin-top: 200px!important;
            }
            .form-contact {
                width: 100%;
            }
            .form-contact-input {
                width: 100%;
                color: #292929;
                font-size: 18px;
                background-color: #E9E9E9;
                border: 1px solid #E9E9E9;
                -moz-border-radius: 5px;
                -webkit-border-radius: 5px;
                border-radius: 5px;
                height: 40px;
                margin-bottom: 20px;
                border-bottom: 1px solid #ccc;
                border-left: 1px solid #ccc;
                text-indent: 20px;
            }
            .form-button {
                width: 100%;
                font-size: 18px;
                border-radius: 4px;
                color: #fff;
                height: 40px;
                opacity: .8;
                margin-bottom: 20px;
                cursor: pointer;
                background: #001d68;
                display: block;
                border: none;
                border-bottom: 1px solid #500707;
                border-right: 1px solid #500707;
                transition: 1s;
            }
            .form-button:hover {
                opacity: 1;
            }
            h1 {
                color: #FFFFFF;
            }
            .liga {
                background: #00AA00;
            }
            .desliga {
                background: #AA0000;
            }
        </style>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Controle do ESP32</title>
    </head>
    <body>
        <div class="container">
            <h1>Controle do ESP32</h1>
            <form action="/liga" class="form-contact" method="post" tabindex="1">
                <button type="submit" class="form-button liga">Ligar</button>
            </form>
            <form action="/desliga" class="form-contact" method="post" tabindex="1">
                <button type="submit" class="form-button desliga">Desligar</button>
            </form>
        </div>
    </body>
</html>
