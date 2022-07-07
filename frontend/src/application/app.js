// This is the scss entry file
import "../styles/index.scss";
import htmx from 'htmx.org/dist/htmx';
import Alpine from 'alpinejs';
import Swiper from 'swiper';

// We can import other JS file as we like
import "../components/sidebar";
import langDropdownMenu from "../components/drop_lang.js";
// import axios from '../components/axiosFactory';
// import { detect } from 'detect-browser';

window.htmx = htmx;
// const browser = detect();

window.document.addEventListener("DOMContentLoaded", function () {
  window.console.log("dom ready 1");
});
window.Alpine = Alpine;
Alpine.data('lang_drop', langDropdownMenu);
// Alpine.data('playlistToggle', playlistToggle);
Alpine.start();

window.Swiper = Swiper;
if (process.env.NODE_ENV === 'development') {
  // enable logging for htmx in development server
  window.htmx.logAll();
}

