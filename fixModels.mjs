import fs from 'fs';

for (let file of ['index.html', 'catalog.html', 'materials.html']) {
    let content = fs.readFileSync(file, 'utf8');

    if (file === 'catalog.html') {
        const startGrid = '<div id="catalog-grid"';
        const iStart = content.indexOf(startGrid);
        if (iStart > -1) {
            // Find the closing bracket of the start tag
            const iTagEnd = content.indexOf('>', iStart) + 1;
            
            // we want to delete everything inside catalog-grid
            // The grid div is inside a container:
            // <div class="max-w-7xl mx-auto px-6 py-12">
            //   <div id="catalog-grid" ...>
            //     ...
            //   </div>
            // </div>
            // </div> <!-- end catalog-page -->
            // <div id="product-page" ...>
            
            const iProduct = content.indexOf('<div id="product-page"');
            if (iProduct > -1) {
                // we want to keep the closing divs. There are 3 closing divs before product-page.
                // Let's find the last </div></div></div> before iProduct
                const closingStr = '</div>\n        </div>\n      </div>\n\n      <div id="product-page"';
                let iEnd = content.indexOf(closingStr);
                if (iEnd === -1) {
                    // Try more robust search
                    const match = content.substring(iTagEnd, iProduct).match(/<\/div>\s*<\/div>\s*<\/div>\s*$/);
                    if (match) {
                        iEnd = iProduct - match[0].length;
                    }
                }
                if (iEnd > -1) {
                    content = content.substring(0, iTagEnd) + '\n            <!-- Javascript will populate this -->\n          ' + content.substring(iEnd);
                } else {
                    console.log("Could not find end of catalog-grid in catalog.html");
                }
            }
        }
    }

    // Fix the image in the JS block so the dynamically generated 10 models show their true images
    const oldImg = '<img src="https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/4734259a-bad7-422f-981e-ce01e79184f2_1600w.jpg" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">';
    const newImg = '<img src="${p.images[0]}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">';
    content = content.replace(oldImg, newImg);
    
    fs.writeFileSync(file, content);
}
console.log('Fix models complete.');
