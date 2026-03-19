import fs from 'fs';

let content = fs.readFileSync('catalog.html', 'utf8');

const startStr = '<div id="catalog-grid"';
const startIndex = content.indexOf(startStr);

if(startIndex > -1) {
    let nOpen = 0;
    let i = startIndex;

    // find first >
    while(content[i] !== '>') i++;
    i++; // move past >

    let contentBefore = content.substring(0, i);

    // Now count
    let substr = content.substring(i);
    let match;
    let re = /<\/?div[^>]*>/g;
    let endGridIndex = -1;

    nOpen = 1; // for catalog-grid itself

    while((match = re.exec(substr)) !== null) {
        if (match[0].startsWith('</div')) {
            nOpen--;
        } else {
            nOpen++;
        }
        if (nOpen === 0) {
            endGridIndex = i + match.index;
            break;
        }
    }

    if (endGridIndex !== -1) {
        content = contentBefore + '\n            <!-- Javascript will populate this -->\n          ' + content.substring(endGridIndex);
        fs.writeFileSync('catalog.html', content);
        console.log("Successfully truncated catalog-grid");
    } else {
        console.log("Failed to parse divs");
    }
} else {
    console.log("Could not find start");
}

