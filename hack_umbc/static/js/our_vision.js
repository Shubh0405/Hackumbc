if (annyang) {
    annyang.addCommands({
        'Go to Home': () => {
            document.getElementById('home_page').click()
        },
        'Go to Voice': () => {
            document.getElementById('revoice_page').click()
        },
        'Go to Synthesizer': () => {
            document.getElementById('synthesiser_page').click()
        },
        'Go to Our Vision': () => {
            document.getElementById('our_vision').click()
        },
        'Scroll Down': () => {
            window.scrollBy(0, 500)
        },
        'Scroll Up': () => {
            window.scrollBy(0, -500)
        },
    });
}

function speakcommand() {
    annyang.start({
        autoRestart: false
    });
}
