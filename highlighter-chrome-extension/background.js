chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "saveHighlight") {
    saveHighlightToServer(request.text);
    saveHighlightToStorage(request.text);
  }
});

function saveHighlightToServer(text) {
  // Replace 'YOUR_API_ENDPOINT' with your actual API endpoint
  console.log("Saving text..", text);
  // fetch('YOUR_API_ENDPOINT', {
  //   method: 'POST',
  //   headers: {
  //     'Content-Type': 'application/json',
  //   },
  //   body: JSON.stringify({ highlight: text }),
  // })
  //     .then(response => response.json())
  //     .then(data => {
  //       console.log('Highlight saved:', data);
  //       // You can add logic here to update storage or send a message to the popup
  //     })
  //     .catch((error) => {
  //       console.error('Error:', error);
  //     });
}

function saveHighlightToStorage(text) {
  chrome.storage.local.get(['recentHighlights'], function(result) {
    let highlights = result.recentHighlights || [];
    highlights.unshift(text); // Add new highlight to the beginning of the array
    highlights = highlights.slice(0, 10); // Keep only the 10 most recent highlights
    chrome.storage.local.set({ recentHighlights: highlights }, function() {
      console.log('Highlight saved to storage:', text);
    });
  });
}