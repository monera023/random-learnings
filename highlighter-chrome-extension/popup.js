document.addEventListener('DOMContentLoaded', function() {
  // Fetch recent highlights from storage and display them
  chrome.storage.local.get(['recentHighlights'], function(result) {
    const highlights = result.recentHighlights || [];
    const list = document.getElementById('highlights-list');
    highlights.forEach(function(highlight) {
      const li = document.createElement('li');
      li.textContent = highlight;
      list.appendChild(li);
    });
  });
});