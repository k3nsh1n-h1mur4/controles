const cbx = document.querySelector('input')

cbx.addEventListener('change', (e) => {
    e.preventDefault();
    console.log(e)
    if (e.target.value === "on") {
        console.log("esta en on")
        const linkElement = document.createElement("a")
        linkElement.href = "/estructura/validate_matricula"
        linkElement.appendChild(document.createTextNode("PASAR"))
        linkElement.setAttribute("class", "btn btn-primary")
        linkElement.setAttribute("margin-left", "5px")
        const divRead = document.getElementById('validate')
        divRead.appendChild(linkElement)
    }
});