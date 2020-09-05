/* Preloader
============================== */
document.body.style.overflow = "hidden";
document.body.onload = function () {
  setTimeout(function () {
    let preloader = document.getElementById('preloader');
    if (!preloader.classList.contains('done')) {
      preloader.classList.add('done');
    }
    document.body.style.overflow = "auto";
  }, 1000);
}

/* Menu
============================== */
let menuBtn = document.querySelector(".menu__btn");
let menuBox = document.querySelector(".menu__box");
let body = document.body;
function MenuScroll() {
  body.style.overflow = "hidden";
  menuBox.style.overflowY = "scroll";
}
function BodyScroll() {
  body.style.overflowY = "scroll";
  menuBox.style.overflow = "hidden";
}
menuBtn.onclick = function() {
  if (menuBox.classList.contains('opened')) {
    menuBox.classList.add('opened');
    MenuScroll();
  } else {
    menuBox.classList.remove('opened');
    BodyScroll();
  }
  if (body.classList.contains('opened')) {
    body.classList.remove('opened');
    BodyScroll();
  } else {
    body.classList.add('opened');
    MenuScroll();
  }
}

/* ProgressBar
============================== */
const progress = document.querySelector('.progress');
window.addEventListener('scroll', progressBar);

function progressBar(e) {
  let windowScroll = document.body.scrollTop || document.documentElement.scrollTop;
  let windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  let per = windowScroll / windowHeight * 100;
  progress.style.width = per + '%';
}

/* Paginator (current)
============================== */
// let header = document.getElementById("paginator");
// let btns = header.getElementsByClassName("paginator__num");
// for (let i = 0; i < btns.length; i++) {
//   btns[i].addEventListener("click", function () {
//     let current = document.getElementsByClassName("current");
//     if (current.length > 0) {
//       current[0].className = current[0].className.replace("current", "");
//     }
//     this.className += " current";
//     this.html('disabled');
//   });
// }

/* Accordion-menu
============================== */
$(function() {
  let Accordion = function(el, multiple) {
    this.el = el || {};
    // more then one submenu open?
    this.multiple = multiple || false;

    let dropdownlink = this.el.find('.dropdownlink');
    dropdownlink.on('click',
                    { el: this.el, multiple: this.multiple },
                    this.dropdown);
  };

  Accordion.prototype.dropdown = function(e) {
    let $el = e.data.el,
        $this = $(this),
        //this is the ul.submenuItems
        $next = $this.next();

    $next.slideToggle();
    $this.parent().toggleClass('open');

    if(!e.data.multiple) {
      //show only one menu at the same time
      $el.find('.submenuItems').not($next).slideUp().parent().removeClass('open');
    }
  }

  let accordion = new Accordion($('.accordion-menu'), false);
})


/* Paginator (-230px)
============================== */
// let pb_start = $("#pb-start");
// let pb_end = $("#pb-end");

// pb_end.hover(function() {
//   pb_start.css("left", "-230px")
//   }, function() {
//   pb_start.css("left", "0");
// });


/* Category
============================== */
// let CategoryItem = $('.category__item');
// let dropdownlink = $('.dropdownlink');
// let submenuItems = $('.submenuItems');

// // dropdownlink.click(function() {
// //   $(this).css('background-color', 'rgba(0, 0, 0, .4)');
// //   }), dropdownlink.click(function() {
// //   $(this).css('background-color', 'none');
// // });


// dropdownlink.on("click", function() {
//   if (submenuItems) {
//     $(this).toggleClass('clicked');
//   }
// });


/* Current-num
============================== */
let material = document.querySelector('#material');
let pagination = document.getElementById('pagination');
let bannerTitle = document.getElementById('banner__title');

if (!material && pagination) {
  let currentNum = document.querySelector('#current-num');
  currentNum.removeAttribute('href');
  currentNum.style.opacity = '1';
  currentNum.style.background = 'rgba(0, 0, 0, .2)';
}

if (material) {
  bannerTitle.style.display = 'none';
}


/* Sidebar settings
============================== */
let sidebar = document.querySelector('#sidebar');

if (material) {
  sidebar.style.height = 'calc(100% + 322px)';
}


/* Fullscreen Search
============================== */
let mobileSearch = document.getElementById('mobile-search');
let searchForm = document.getElementById('search-form');
let headerInput = document.getElementById('header__input');
let bannerBackground = document.getElementById('banner-background');

mobileSearch.addEventListener("click", function() {
  if(searchForm.style.display == 'block') {
    searchForm.style.display = 'none';
    bannerBackground.classList.remove('banner-before');
  }
  else {
    searchForm.style.display = 'block';
    bannerBackground.classList.add('banner-before');
    headerInput.focus();
  }
});

function showForm(){ if(x.matches) searchForm.style.display = 'block'; }
function hideForm(){ if(f.matches) searchForm.style.display = 'none'; }

let x = window.matchMedia("(min-width: 1199px)");
showForm();
x.addListener(showForm);

let f = window.matchMedia("(max-width: 1199px)");
hideForm();
f.addListener(hideForm);


































