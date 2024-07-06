async function sendPostRequest() {
    var textarea = document.getElementById('text_input');
    var text = textarea.value;
    var data = new URLSearchParams();
    data.append('text', text);
    var response = await fetch('/get_word', {
        method: 'POST',
        body: data
    });
    var word = await response.text();
    var h1_answer = document.getElementById('answer');
    h1_answer.textContent = "Вердикт: " + word;
}