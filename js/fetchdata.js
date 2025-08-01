function fetchData(url, elementId) {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            const el = document.getElementById(elementId);
            if (!el) {
                console.warn(`Element with ID "${elementId}" not found.`);
                return;
            }
            const values = Object.values(data);
            if (values.length > 0) {
                el.innerText = values[0];
            } else {
                el.innerText = 'No data available';
            }
        })
        .catch(error => {
            console.error('Error fetching data:', error);
            const el = document.getElementById(elementId);
            if (el) {
                el.innerText = 'Bot offline';
            }
        });
}
