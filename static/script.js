async function improveCommit() { 
    let input = document.getElementById("input").value; 
 
    let response = await fetch("/improve", { 
        method: "POST", 
        headers: { 
            "Content-Type": "application/json" 
        }, 
        body: JSON.stringify({ msg: input }) 
    }); 
 
    let data = await response.json(); 
    document.getElementById("output").innerText = data.result; 
} 
 
function copyText() { 
    let text = document.getElementById("output").innerText; 
    navigator.clipboard.writeText(text); 
    alert("Copied!"); 
}
