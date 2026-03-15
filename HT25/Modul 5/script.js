document.addEventListener("DOMContentLoaded", () => {
  const header = document.querySelector("header");
  const footer = document.querySelector("footer");

  if (header) {
    header.innerHTML = `
            LÄGG TILL DIN HEADER-HÄR
        `;
  }

  if (footer) {
    footer.innerHTML = `
            LÄGG TILL DIN FOOTER-HÄR
        `;
  }
});
