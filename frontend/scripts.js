// Frontend logic for the expanded Acute Music app

// Fetch homepage data from backend
async function loadHomepage() {
    try {
        const response = await fetch('/api/homepage');
        const data = await response.json();

        document.getElementById('totalSongs').innerText = data.totalSongs;
        populateList('trendingSongs', data.trending);
        populateList('popularSongs', data.popular);
    } catch (error) {
        console.error('Error fetching homepage data:', error);
    }
}

// Populate a list with song data
function populateList(elementId, songs) {
    const list = document.getElementById(elementId);
    list.innerHTML = '';
    songs.forEach(song => {
        const li = document.createElement('li');
        li.innerText = song.title + " by " + song.artist;
        list.appendChild(li);
    });
}

// Handle playlist creation
document.getElementById('createPlaylistForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const playlistName = document.getElementById('playlistName').value;
    try {
        const response = await fetch('/api/playlists', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name: playlistName }),
        });
        if (response.ok) {
            alert('Playlist created!');
        } else {
            alert('Failed to create playlist');
        }
    } catch (error) {
        console.error('Error creating playlist:', error);
    }
});

// Load homepage on startup
loadHomepage();