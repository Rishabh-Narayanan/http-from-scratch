window.onload = () => {
	const btn = document.getElementById("alert-button");
	if (btn) {
		btn.onclick = (e) => {
			alert("Hello World!");
		};
	}
}
