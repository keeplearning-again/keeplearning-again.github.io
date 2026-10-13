'use strict';

// Publications remain server-rendered and readable when JavaScript is unavailable.
const filters = [...document.querySelectorAll('[data-filter]')];
const papers = [...document.querySelectorAll('.publication')];
const yearGroups = [...document.querySelectorAll('.publication-year-group')];
const counter = document.querySelector('.publication-count');
document.querySelectorAll('[data-js-only]').forEach(element => { element.hidden = false; });

filters.forEach(button => {
  button.addEventListener('click', () => {
    const topic = button.dataset.filter;
    filters.forEach(filter => filter.setAttribute('aria-pressed', String(filter === button)));
    let visible = 0;
    papers.forEach(paper => {
      paper.hidden = topic !== 'All' && !JSON.parse(paper.dataset.topics).includes(topic);
      if (!paper.hidden) visible += 1;
    });
    yearGroups.forEach(group => {
      const count = [...group.querySelectorAll('.publication')].filter(paper => !paper.hidden).length;
      group.hidden = count === 0;
      group.querySelector('.year-heading span').textContent = `${count} ${count === 1 ? 'paper' : 'papers'}`;
    });
    counter.textContent = `${visible} ${visible === 1 ? 'publication' : 'publications'} · newest first`;
  });
});
