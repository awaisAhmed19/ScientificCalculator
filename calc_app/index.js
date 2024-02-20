const { app, BrowserWindow } = require('electron');

let Win;

function createWindow() {
    Win = new BrowserWindow({
        width: 700,
        height: 1200,
        webPreferences: {
            nodeIntegration: true
        }
    });

    Win.loadFile('calc_app/index.html');
}

app.on('ready', createWindow);

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

app.on('activate', function () {
    if (Win === null) createWindow();
});
