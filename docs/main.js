  /*
  Project: Indiana Jones and the Fountain of Youth (indy-foy)
  File: main.js
  Version: 0.1.1
  Description: Handles accordion panels, lightbox viewer, and roadmap progress calculation.
  
  Author: Erek Starwind (BYTE RANGER Software)
  Edited: 2025-08-27
*/
const panels = Array.from(document.querySelectorAll('.panel'));
function activateById(id){ panels.forEach(p=>p.classList.toggle('active', '#'+p.id===id)); if(history&&history.replaceState) history.replaceState(null,'',id); }
function initAccordion(){
  const valid = h => panels.some(p => '#'+p.id===h);
  activateById(valid(location.hash)?location.hash:'#intro');
  panels.forEach(p=>p.addEventListener('click',e=>{ if(!(e.target.closest&&e.target.closest('.content'))) activateById('#'+p.id); }));
  addEventListener('hashchange',()=>activateById(valid(location.hash)?location.hash:'#intro'));
}
function initLightbox(){
  const lb=document.getElementById('lb'), img=document.getElementById('lbImg'), cap=document.getElementById('lbCap'), btn=document.getElementById('lbClose');
  const open=(src,c)=>{ img.src=src; img.alt=c||''; cap.textContent=c||''; lb.classList.add('open'); lb.setAttribute('aria-hidden','false'); };
  const close=()=>{ lb.classList.remove('open'); lb.setAttribute('aria-hidden','true'); img.src=''; cap.textContent=''; };
  document.addEventListener('click',e=>{ const a=e.target.closest&&e.target.closest('a[data-lightbox]'); if(a){ e.preventDefault(); open(a.getAttribute('href'), a.dataset.caption);} });
  lb.addEventListener('click',e=>{ if(e.target===lb) close();}); btn.addEventListener('click',close); document.addEventListener('keydown',e=>{ if(e.key==='Escape') close(); });
}

function initRoadmap(){
  const milestones = document.querySelectorAll('.ms');

  milestones.forEach(ms=>{
    const tasks = ms.querySelectorAll('.tasks li');
    const total = tasks.length || 1;
    let progress = 0;

    tasks.forEach(li=>{
      const s = (li.dataset.status || 'todo').toLowerCase();
      if (s === 'done') {
        progress += 1;            // voller Task
      } else if (s === 'doing') {
        progress += 0.25;         // nur 1/4 Task
      }
    });

    const pct = Math.round((progress / total) * 100);

    const bar   = ms.querySelector('.bar');
    const pctEl = ms.querySelector('.pct');
    const badge = ms.querySelector('.badge');

    if (bar)   bar.style.width = pct + '%';
    if (pctEl) pctEl.textContent = pct + '%';

    if (pct === 100) {
      badge.textContent = 'Done';
      badge.className   = 'badge done';
    } else if (pct > 0) {
      badge.textContent = 'In Progress';
      badge.className   = 'badge doing';
    } else {
      badge.textContent = 'Planned';
      badge.className   = 'badge todo';
    }
  });
}

document.addEventListener('DOMContentLoaded',()=>{ initAccordion(); initLightbox(); initRoadmap(); });