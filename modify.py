import re

with open('materials.html', 'r', encoding='utf-8') as f:
    content = f.read()

materials_html_replacement = '''<div id="materials-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <!-- Dynamically generated materials will go here -->
          </div>
        </div>
      </div>

      <!-- Modal for Materials -->
      <div id="material-modal" class="fixed inset-0 z-[60] flex items-center justify-center p-4 sm:p-6 bg-zinc-900/80 backdrop-blur-sm transition-all duration-300 opacity-0 pointer-events-none hidden" onclick="if(event.target === this) closeMaterialModal()">
        <div class="bg-white rounded-2xl w-full max-w-4xl overflow-hidden shadow-2xl transform scale-95 transition-transform duration-300 flex flex-col md:flex-row relative">
          <button onclick="closeMaterialModal()" class="absolute top-4 right-4 z-10 w-8 h-8 flex items-center justify-center bg-white/80 backdrop-blur-md rounded-full text-zinc-900 hover:bg-zinc-100 transition-colors focus:outline-none">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="m16 8l-8 8m0-8l8 8m9-4a9 9 0 1 1-18 0a9 9 0 0 1 18 0Z"/></svg>
          </button>
          <div class="md:w-1/2 bg-zinc-100 flex items-center justify-center relative min-h-[300px] md:min-h-0">
            <img id="modal-material-img" src="" alt="Material" class="absolute inset-0 w-full h-full object-cover">
          </div>
          <div class="md:w-1/2 p-8 md:p-12 flex flex-col justify-center bg-white">
            <h2 id="modal-material-title" class="text-2xl md:text-3xl font-medium tracking-tight text-zinc-900 uppercase mb-4"></h2>
            <p id="modal-material-desc" class="text-zinc-600 text-sm md:text-base leading-relaxed"></p>
          </div>
        </div>
      </div>

      <!-- PAGE: PRIVACY POLICY -->'''

content = re.sub(
    r'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">.*?<!-- PAGE: PRIVACY POLICY -->', 
    materials_html_replacement, 
    content, 
    flags=re.DOTALL
)

js_materials_list = """// --- Materials Data ---
      const materialsList = [
          {
              name: "Negro Marquina",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/d0c3fabb-7b69-4500-8fb8-69f799c0f2c9_800w.jpg",
              desc: "Элегантный черный мрамор с контрастными белыми прожилками. Идеален для создания строгих и стильных интерьеров."
          },
          {
              name: "Orobico Rosso (Rosso Fendi)",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/3e8232c3-4e23-490b-9786-1ed4a432e4e2_800w.jpg",
              desc: "Роскошный итальянский мрамор с уникальным рисунком из красных, серых и золотистых оттенков, напоминающий живописные полотна."
          },
          {
              name: "VOLAKAS",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/fbec44d6-c147-4078-800a-1d427434c323_800w.jpg",
              desc: "Классический белый мрамор из Греции с мягкими, струящимися серыми прожилками. Придает пространству легкость и аристократизм."
          },
          {
              name: "Exotic Black",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/b2c57cab-e80d-45fe-885b-c9e53f5203d6_800w.jpg",
              desc: "Выразительный темный гранит с глубокой текстурой и необычными вкраплениями, подчеркивающими природную мощь камня."
          },
          {
              name: "ARABESCATO GRIGIO OROBICO",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/a1157770-f8d0-462e-aede-989e41607579_800w.jpg",
              desc: "Эксклюзивный итальянский мрамор со сложным, затейливым узором в серых и бежевых тонах."
          },
          {
              name: "ARABESCATO GRIGIO OROBICO",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/f2fa7552-fa15-4ddd-bdf0-3132623f8ff9_800w.jpg",
              desc: "Эффектный мрамор с динамичным рисунком, создающий неповторимую игру света и тени в интерьере."
          },
          {
              name: "PIETRA GREY",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/690a11fc-51df-4d72-bdb0-423cd99e493e_800w.jpg",
              desc: "Благородный графитово-серый мрамор с тонкими, изящными белыми линиями. Отличный выбор для современных минималистичных дизайнов."
          },
          {
              name: "ROSSO LEVANTO",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/a53aed52-84b1-4a37-b5df-8f5172003ff0_800w.jpg",
              desc: "Насыщенный вишнево-красный мрамор из Италии с густой сетью белых прожилок. Привносит в интерьер драматизм и статусность."
          },
          {
              name: "STATUARIETTO",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/733cdb8d-9319-45e8-9a3a-272094e77074_800w.jpg",
              desc: "Утонченный белый мрамор с деликатным серым рисунком. Ценится за чистоту фона и элегантную текстуру."
          },
          {
              name: "SILVER WAVE",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/9b9abf65-7c16-46fc-9e09-a2e8b5e199e6_800w.jpg",
              desc: "Мрамор с завораживающим линейным узором, напоминающим серебристые волны на темном фоне."
          },
          {
              name: "PIRGON",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/ae42eb1f-abb7-49de-bbe5-7a69b34a54aa_800w.jpg",
              desc: "Нежный белый мрамор с легкими облачными включениями, придающий поверхности визуальную мягкость и объем."
          },
          {
              name: "Rouge Epique",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/9529b12c-5fb1-4bfc-8add-d46292c32ecf_800w.jpg",
              desc: "Экстравагантный камень глубоких красно-бордовых оттенков, который станет ярким акцентом в любом пространстве."
          },
          {
              name: "ALEXANDRA BLACK",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/6d7afd4d-808c-45e1-8a83-5bd6cbc605fe_800w.jpg",
              desc: "Строгий черный камень с загадочной текстурой, идеальный для создания контрастных и респектабельных интерьеров."
          },
          {
              name: "Травертин CLASSIC VEIN CUT",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/3b5d1677-9f81-47e8-ac42-c7717d03d3d6_800w.jpg",
              desc: "Традиционный бежевый травертин с продольным распилом, подчеркивающим полосатую текстуру, созданную самой природой."
          },
          {
              name: "CALACATTA ORO",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/fd680790-d2b5-48e0-ab88-55ee03a0b7f0_800w.jpg",
              desc: "Премиальный итальянский мрамор с теплым белым фоном и изысканными золотисто-серыми прожилками, воплощение роскоши."
          },
          {
              name: "Травертин SILVER",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/3e0b3320-7664-423c-8333-780265a02062_800w.jpg",
              desc: "Элегантный травертин в прохладных серебристо-серых тонах, сочетающий природную фактуру с современным цветовым решением."
          },
          {
              name: "Травертин STRIATO FILLED HONED",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/08ef6bb0-1577-46ac-be53-b6ea31fb1ec6_800w.jpg",
              desc: "Лощеный итальянский травертин с продольным рисунком (Striato) и заполненными порами для гладкой, теплой поверхности."
          },
          {
              name: "Травертин IVORY",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/099815b5-3751-4ad8-a5bd-5d8dacdcd657_800w.jpg",
              desc: "Светлый, оттенок слоновой кости, травертин, наполняющий помещение светом и ощущением природного тепла."
          },
          {
              name: "Травертин STRIATO UNFILLED HONED",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/475fbe2f-a0c3-4346-912e-06f2d15f05b8_800w.jpg",
              desc: "Травертин с открытыми порами и четко выраженной слоистой структурой, раскрывающий всю естественную красоту камня."
          },
          {
              name: "Traonyx",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/1e8ca7f9-118b-4b47-b767-45be94e26ef3_800w.jpg",
              desc: "Удивительное сочетание слоистого травертина и полупрозрачного оникса в одном камне, создающее богатство фактур."
          },
          {
              name: "Оникс GREY",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/e7e67341-30d1-4657-aa47-cb990cc65f29_800w.jpg",
              desc: "Редкий серый оникс, обладающий светопропускной способностью. Идеально подходит для эффектных порталов с подсветкой."
          },
          {
              name: "Оникс VERDE",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/44a0e496-63e4-497b-915c-7ddd1a387d9c_800w.jpg",
              desc: "Классический зеленый оникс с живописными слоистыми переходами от глубокого изумрудного до нежно-салатового."
          },
          {
              name: "Оникс GOLDEN TIGER",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/0fb8f2e3-6240-4f65-8bf4-c454e4acbcac_800w.jpg",
              desc: "Поистине роскошный камень с янтарными и золотистыми полосами, напоминающими окрас тигра и излучающий тепло."
          },
          {
              name: "Оникс TERRA BLUE",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/50423239-7dcf-4476-a0c2-2d3cf584ee84_800w.jpg",
              desc: "Экзотический оникс с уникальными голубоватыми и землистыми оттенками, создающий атмосферу магии и умиротворения."
          },
          {
              name: "Оникс WHITE LINES",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/58ff174b-d04d-4cde-83ee-90806bd8fff2_800w.jpg",
              desc: "Белоснежный оникс с тонкими, едва уловимыми линиями, поражающий своей чистотой и способностью светиться изнутри."
          },
          {
              name: "Silver Roots",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/28808e0f-afe7-42d3-9791-1fd727151bbf_800w.jpg",
              desc: "Мрамор с невероятной паутиной серебристых 'корней' на темном фоне, добавляющий интерьеру брутальности и характера."
          },
          {
              name: "Травертин Jurassic",
              image: "https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/43f9db38-8f4f-4f1d-b21e-a7097fd89ca6_800w.jpg",
              desc: "Уникальный травертин с ярко выраженными отпечатками древних эпох, настоящий природный артефакт в вашем доме."
          }
      ];

      function openMaterialModal(index) {
          const material = materialsList[index];
          if(!material) return;
          document.getElementById('modal-material-title').innerText = material.name;
          document.getElementById('modal-material-desc').innerText = material.desc;
          document.getElementById('modal-material-img').src = material.image;
          
          const modal = document.getElementById('material-modal');
          const modalInner = modal.querySelector('div.bg-white');
          
          modal.classList.remove('hidden');
          setTimeout(() => {
              modal.classList.remove('opacity-0', 'pointer-events-none');
              modalInner.classList.remove('scale-95');
              modalInner.classList.add('scale-100');
          }, 10);
      }

      function closeMaterialModal() {
          const modal = document.getElementById('material-modal');
          const modalInner = modal.querySelector('div.bg-white');
          
          modal.classList.add('opacity-0', 'pointer-events-none');
          modalInner.classList.add('scale-95');
          modalInner.classList.remove('scale-100');
          
          setTimeout(() => {
              modal.classList.add('hidden');
          }, 300);
      }

      // --- Init Catalog ---
      const grid = document.getElementById('catalog-grid');"""

content = re.sub(
    r'// --- Init Catalog ---\s*const grid = document.getElementById\(\'catalog-grid\'\);',
    js_materials_list,
    content
)

js_materials_init = """if (grid) {
          products.forEach(p => {
              grid.innerHTML += `
                  <div onclick="openProduct(${p.id})" class="group cursor-pointer">
                      <div class="aspect-[4/5] bg-zinc-100 rounded-xl overflow-hidden mb-4 relative">
                          <img src="${p.images[0]}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                          <div class="absolute bottom-4 right-4 bg-white/90 backdrop-blur-sm px-3 py-1.5 rounded-lg text-xs font-medium text-zinc-900 shadow-sm opacity-0 group-hover:opacity-100 transition-opacity translate-y-2 group-hover:translate-y-0 duration-300">
                              от ${p.price} ₽
                          </div>
                      </div>
                      <h3 class="text-base font-medium text-zinc-900">${p.name}</h3>
                      <p class="text-xs text-zinc-500 mt-1">${p.cat}</p>
                  </div>
              `;
          });
      }

      const materialsGrid = document.getElementById('materials-grid');
      if (materialsGrid) {
          materialsList.forEach((m, idx) => {
              materialsGrid.innerHTML += `
                  <div onclick="openMaterialModal(${idx})" class="group cursor-pointer">
                    <div class="aspect-square rounded-2xl overflow-hidden bg-zinc-100 mb-4 relative border border-zinc-100">
                      <img src="${m.image}" alt="${m.name}" class="group-hover:scale-105 transition-transform duration-700 w-full h-full object-cover">
                    </div>
                    <h3 class="text-lg font-medium text-zinc-900 uppercase">
                      ${m.name}
                    </h3>
                  </div>
              `;
          });
      }"""

content = re.sub(
    r'if\s*\(grid\)\s*\{\s*products.forEach\(p => \{.*?\}\);\s*\}',
    js_materials_init,
    content,
    flags=re.DOTALL
)

with open('materials.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated materials.html successfully")
