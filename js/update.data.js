// Call fetchData to update specific elements

document.addEventListener('DOMContentLoaded', () => {
    fetchInitialUptime('http://localhost:9921/uptime');
    if (document.getElementById('ping-info')) {
        fetchData('/ping', 'ping');
    }
    if (document.getElementById('guilds-info')) {
        fetchData('/guilds', 'guilds');
    }
});
