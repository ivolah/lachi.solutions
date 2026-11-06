// Language selector: remembers the chosen language and makes links work from file://.
(function () {
  var lang = document.documentElement.lang;
  try { localStorage.setItem("ls-lang", lang); } catch (e) {}
  if (location.protocol === "file:") {
    var links = document.querySelectorAll('a[href$="/"]');
    for (var i = 0; i < links.length; i++) links[i].href += "index.html";
  }
})();
