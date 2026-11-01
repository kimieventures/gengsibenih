const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
const [file,...ts]=process.argv.slice(2);
await p.goto('file://'+file);await p.waitForTimeout(600);
for(const t of ts){await p.evaluate(t=>render(+t),t);await p.screenshot({path:`out/st_${require('path').basename(file,'.html')}_${t}.jpg`,type:'jpeg',quality:70});}
await b.close();})();
