document.addEventListener('mouseup', function() {
  let selectedText = window.getSelection().toString().trim();
  if (selectedText.length > 0) {
    highlightText(selectedText);
    chrome.runtime.sendMessage({action: "saveHighlight", text: selectedText, url: window.location.href});
  }
});

function highlightText(text) {
  let range = window.getSelection().getRangeAt(0);
  let newNode = document.createElement("span");
  newNode.setAttribute("style", "background-color: yellow;");
  range.surroundContents(newNode);
}