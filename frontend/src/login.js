const form = document.querySelector("form");
form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const id = document.querySelector("input#id").value;
  const password = document.querySelector("input#password").value;
  const response = await fetch("http://localhost:9000/api/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ id, password }),
  });
  console.log(response);
});
