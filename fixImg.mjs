import fs from 'fs';

for (let file of ['index.html', 'catalog.html', 'materials.html']) {
    let content = fs.readFileSync(file, 'utf8');
    
    content = content.replace(
        '<img src="https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/4734259a-bad7-422f-981e-ce01e79184f2_1600w.jpg"',
        '<img src="${p.images[0]}"'
    );
    
    fs.writeFileSync(file, content);
}
console.log('Images fixed.');
