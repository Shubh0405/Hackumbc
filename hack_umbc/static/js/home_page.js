if (annyang) {
    const commands = {
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
        'Scroll Down': () => {
            window.scrollBy(0, -500)
        },
    };

    // Add our commands to annyang
    annyang.addCommands(commands);
}

function speakcommand() {
    annyang.start({
        autoRestart: false
    });
}
