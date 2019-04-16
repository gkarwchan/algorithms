'use strict';

// Complete the sockMerchant function below.
function sockMerchant(n, ar) {
    if (ar.length > n) {
        ar.splice(n)
    }
    const socksByColorsTotal = ar.reduce((socksByColors, sock) => {
        if (isNaN(sock)) return socksByColors;
        if (socksByColors[sock]) {
            socksByColors[sock]++;
        } else {
            socksByColors[sock] = 1;
        }
        return socksByColors
    }, {});
    return Object.values(socksByColorsTotal).map(val => Math.floor(val / 2))
        .reduce((sum, val) => sum += val, 0)
}
