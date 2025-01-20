function alertMessage() 
{
    alert('Hello from Flask Front-End!');
}

function startCameras() {
    fetch('/start-video', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function aboutRoute()
{
    window.location.href = '/about'; 
}

function startVideo() {
    // Open a new popup window for the video feed
    const popup = window.open("", "VideoStream", "width=800,height=600");
    if (popup) {
        popup.document.write(`
            <html>
            <body>
                <h1>Video Stream</h1>
                <img id="videoFeed" src="/video_feed" style="width:100%;border:1px solid black;" />
            </body>
            </html>
        `);

        // Automatically close the popup when the user clicks the X button
        popup.onbeforeunload = () => {
            console.log("Popup closed");
        };
    } else {
        alert("Popup blocked. Please allow popups for this site.");
    }
}

function takePhoto()
{
    window.location.href = '/take_photo';
}
