document.addEventListener('DOMContentLoaded', () =>{

    document.querySelector('.close').onclick = () =>{
        document.querySelector('.close').parentElement.remove();
    }
});