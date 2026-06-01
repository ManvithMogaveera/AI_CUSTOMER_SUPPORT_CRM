const API = "https://ai-customer-support-crm.onrender.com";
 
/* ── Badge helpers ── */
 
const CATEGORY_CLASSES = {
    "Technical Issue":      "badge-technical",
    "Billing Inquiry":      "badge-billing",
    "Refund Request":       "badge-refund",
    "Product Inquiry":      "badge-product",
    "Cancellation Request": "badge-cancel"
};
 
const STATUS_CLASSES = {
    "Open":        "badge-open",
    "In Progress": "badge-progress",
    "Closed":      "badge-closed"
};
 
const categoryBadge = (cat) =>
    `<span class="badge ${CATEGORY_CLASSES[cat] ?? "badge-cancel"}">${cat ?? "Unknown"}</span>`;
 
const statusBadge = (status) =>
    `<span class="badge ${STATUS_CLASSES[status] ?? "badge-cancel"}">${status}</span>`;
 
 
/* ── Toast ── */
 
let toastTimer;
 
function showToast(msg, type = "success") {
    const toast = document.getElementById("toast");
    toast.textContent = msg;
    toast.className = `toast-msg toast-${type} show`;
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toast.classList.remove("show"), 3000);
}
 
 
/* ── Modal ── */
 
function openModal()  { document.getElementById("ticketModal").classList.add("active"); }
function closeModal() { document.getElementById("ticketModal").classList.remove("active"); }
 
// Close modal on backdrop click
document.getElementById("ticketModal").addEventListener("click", (e) => {
    if (e.target === e.currentTarget) closeModal();
});
 
// Close modal on Escape key
document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeModal();
});
 
 
/* ── API helper ── */
 
async function apiFetch(path, options = {}) {
    const res = await fetch(`${API}${path}`, {
        headers: { "Content-Type": "application/json" },
        ...options
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return res.json();
}
 
 
/* ── Create ticket ── */
 
async function createTicket() {
    const get = (id) => document.getElementById(id).value.trim();
 
    const data = {
        customer_name:  get("name"),
        customer_email: get("email"),
        subject:        get("subject"),
        description:    get("description")
    };
 
    if (!data.customer_name || !data.subject) {
        showToast("Name and subject are required", "error");
        return;
    }
 
    try {
        const result = await apiFetch("/api/tickets", {
            method: "POST",
            body: JSON.stringify(data)
        });
 
        showToast(`✅ Category predicted: ${result.category}`);
        ["name", "email", "subject", "description"].forEach(id => {
            document.getElementById(id).value = "";
        });
        loadTickets();
 
    } catch {
        showToast("❌ Could not connect to API", "error");
    }
}
 
 
/* ── Load & render tickets ── */
 
async function loadTickets() {
    const search = encodeURIComponent(document.getElementById("searchInput").value);
    const status = encodeURIComponent(document.getElementById("statusFilter").value);
 
    try {
        const tickets = await apiFetch(`/api/tickets?search=${search}&status=${status}`);
 
        document.getElementById("totalTickets").textContent  = tickets.length;
        document.getElementById("openTickets").textContent   = tickets.filter(t => t.status === "Open").length;
        document.getElementById("closedTickets").textContent = tickets.filter(t => t.status === "Closed").length;
 
        const tbody = document.getElementById("ticketTable");
 
        if (!tickets.length) {
            tbody.innerHTML = `<tr><td colspan="6" class="text-center text-muted py-4">No tickets found</td></tr>`;
            return;
        }
 
        tbody.innerHTML = tickets.map(t => `
            <tr>
                <td style="color:#aaa; font-size:0.78rem">${t.ticket_id}</td>
                <td>
                    <div class="cust-name">${t.customer_name}</div>
                    <div class="cust-email">${t.customer_email ?? ""}</div>
                </td>
                <td>${t.subject}</td>
                <td>${categoryBadge(t.category)}</td>
                <td>${statusBadge(t.status)}</td>
                <td>
                    <div class="action-btns">
                        <button class="btn btn-view"     onclick="viewTicket('${t.ticket_id}')">View</button>
                        <button class="btn btn-progress" onclick="setStatus('${t.ticket_id}', 'In Progress')">Progress</button>
                        <button class="btn btn-close"    onclick="setStatus('${t.ticket_id}', 'Closed')">Close</button>
                        ${t.status === "Closed"
                            ? `<button class="btn btn-delete" onclick="deleteTicket('${t.ticket_id}')">Delete</button>`
                            : ""}
                    </div>
                </td>
            </tr>
        `).join("");
 
    } catch {
        document.getElementById("ticketTable").innerHTML =
            `<tr><td colspan="6" class="text-center text-muted py-4">⚠ Could not load tickets — is the API running?</td></tr>`;
    }
}
 
 
/* ── View ticket ── */
 
async function viewTicket(id) {
    try {
        const t = await apiFetch(`/api/tickets/${id}`);
 
        document.getElementById("modalContent").innerHTML = `
            <div class="modal-row"><span class="modal-label">Ticket ID</span>  <span class="modal-val">${t.ticket_id}</span></div>
            <div class="modal-row"><span class="modal-label">Customer</span>   <span class="modal-val">${t.customer_name}</span></div>
            <div class="modal-row"><span class="modal-label">Email</span>      <span class="modal-val">${t.customer_email}</span></div>
            <div class="modal-row"><span class="modal-label">Subject</span>    <span class="modal-val">${t.subject}</span></div>
            <div class="modal-row"><span class="modal-label">Description</span><span class="modal-val">${t.description}</span></div>
            <div class="modal-row"><span class="modal-label">Category</span>   <span class="modal-val">${categoryBadge(t.category)}</span></div>
            <div class="modal-row"><span class="modal-label">Status</span>     <span class="modal-val">${statusBadge(t.status)}</span></div>
        `;
 
        openModal();
 
    } catch {
        showToast("❌ Could not load ticket", "error");
    }
}
 
 
/* ── Update status ── */
 
async function setStatus(id, status) {
    try {
        await apiFetch(`/api/tickets/${id}`, {
            method: "PUT",
            body: JSON.stringify({ status })
        });
        loadTickets();
    } catch {
        showToast("❌ Could not update ticket", "error");
    }
}
 
 
/* ── Delete ticket ── */
 
async function deleteTicket(id) {
    if (!confirm("Delete this ticket permanently?")) return;
 
    try {
        await apiFetch(`/api/tickets/${id}`, { method: "DELETE" });
        showToast("🗑 Ticket deleted");
        loadTickets();
    } catch {
        showToast("❌ Could not delete ticket", "error");
    }
}
 
 
/* ── Init ── */
loadTickets();
