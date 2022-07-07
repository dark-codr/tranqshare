export default function langDropdownMenu() {
    return {
        openMenu: false,
        deposit: false,
        lang: false,
        copy: false,

        toggleOpen() {
            this.openMenu = !this.openMenu;
            const menu = document.getElementById("lang");
            const icon = document.getElementById("lang_icon");
            menu.classList.toggle("hidden");
            icon.classList.toggle("mt-2");
        },

        toggleClose() {
            const menu = document.getElementById("lang");
            const icon = document.getElementById("lang_icon");
            menu.classList.add("hidden");
            icon.classList.toggle("mt-0");
            return this.openMenu = false;
        },

        open() {
            this.deposit = !this.deposit;
            const menu = document.getElementById("depo");
            menu.classList.toggle("hidden");
        },

        close() {
            const menu = document.getElementById("depo");
            menu.classList.add("hidden");
            return this.deposit = false;
        },

        wdropen() {
            this.deposit = !this.deposit;
            const menu = document.getElementById("wdr");
            menu.classList.toggle("hidden");
        },

        wdrclose() {
            const menu = document.getElementById("wdr");
            menu.classList.add("hidden");
            return this.deposit = false;
        },

        wopen() {
            this.deposit = !this.deposit;
            const menu = document.getElementById("wdepo");
            const old = document.getElementById("depo");
            old.classList.add("hidden");
            menu.classList.toggle("hidden");
        },

        wclose() {
            const menu = document.getElementById("wdepo");
            menu.classList.add("hidden");
            return this.deposit = false;
        },

        cookiesClose() {
            const cookie = document.getElementById("cookie");
            cookie.classList.remove("md:flex", "md:items-center");
            cookie.classList.add("hidden", "md:hidden");
            return this.lang = true;
        },

        wcopy() {
            this.copy = !this.copy;
            const menu = document.getElementById("copy");
            menu.select();
            menu.setSelectionRange(0, 99999);
            navigator.clipboard.writeText(menu.value);
            alert("Copied the text: " + menu.value);
        }


    };
}
