partes = {
    cabeca: "/static/guitarras/images/partes/cabecas/{}.svg",
    braco: "/static/guitarras/images/partes/bracos/{}.svg",
    corpo: "/static/guitarras/images/partes/corpos/{}.svg",
    capitador1: "/static/guitarras/images/partes/capitadores/{}.svg",
    capitador2: "/static/guitarras/images/partes/capitadores/{}.svg",
}

trocaParte=(x, y)=>document.getElementById(x).src=partes[x].replace('{}', y.target.value)

for (let i in partes)
    document.getElementById('id_'+i).addEventListener("change", trocaParte.bind(this, i))

function generateImage() {
    let canvas = document.createElement('canvas');
    let context = canvas.getContext('2d');

    canvas.setAttribute('width', 584/2);
    canvas.setAttribute('height', 1036/2);
    context.scale(.5, .5);

    for (let i in partes)
        context.drawImage(document.getElementById(i), 0, 0);

    document.getElementById('id_imagem').value = canvas.toDataURL();

    document.guitarraForm.submit();
}
