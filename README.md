# microsservicoCustomBlock
Microsservico para CustomBlock

<style>
    #title {
        width: 30px;
        height:30px
    }

</style>
<p id="title">How to use it:</p> 

Apensar pegue o seguinte formato JSON: <br>
{
    "client_id": "xxxx",
    "client_secret": "xxxx",
    "external_key": "xxxx",
    "mid": "xxxx"
}
<br>

Substitua os "x" pelas informações do Marketing Cloud:
Client_id -> ClientId dentro do Installed Package
Client_secret: -> ClientSecret dentro do Installed Package
external_key: ExternalKey da Data Extension que deseja consultar os atributos
mid: MID (ou ID) da BU que essa DE está situada.