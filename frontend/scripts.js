// Fetch homepage data from backend
window.onload = async () => {
    try {
        const response = await fetch('/api/homepage');
        const data = await response.json();

        document.getElementById('totalSongs').innerText = data.totalSongs;
        populateList('trendingSongs', data.trending);
        populateList('popularSongs', data.popular);
    } catch (error) {
        console.error('Error fetching homepage data:', error);
    }
};

function populateList(elementId, songs) {
    const list = document.getElementById(elementId);
    list.innerHTML = '';
    songs.forEach(song => {
        const li = document.createElement('li');
        li.innerText = song;
        list.appendChild(li);
    });
}