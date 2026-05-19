"""Generate the new premium login page."""
import os
BASE = os.path.dirname(os.path.abspath(__file__))
TMPL = os.path.join(BASE, "app", "templates")

login_html = r'''{% extends "base.html" %}
{% block title %}Sign In — SynavueDev{% endblock %}

{% block head %}
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
@keyframes pulse-glow{0%,100%{box-shadow:0 0 20px rgba(245,158,11,0.15)}50%{box-shadow:0 0 40px rgba(245,158,11,0.3)}}
@keyframes blink{50%{border-color:transparent}}
@keyframes gradient-shift{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
@keyframes fade-in-up{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:translateY(0)}}
@keyframes shimmer{0%{background-position:-200% 0}100%{background-position:200% 0}}
@keyframes border-glow{0%,100%{border-color:rgba(245,158,11,0.08)}50%{border-color:rgba(245,158,11,0.2)}}
.float-1{animation:float 6s ease-in-out infinite}
.float-2{animation:float 8s ease-in-out infinite 1s}
.float-3{animation:float 7s ease-in-out infinite 2s}
.pulse-glow{animation:pulse-glow 3s ease-in-out infinite}
.fade-in{animation:fade-in-up 0.5s ease-out both}
.fade-d1{animation-delay:.1s}.fade-d2{animation-delay:.2s}.fade-d3{animation-delay:.3s}.fade-d4{animation-delay:.4s}
.page-bg{background:#080812 !important;position:relative;overflow:hidden}
.page-bg::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 80% 60% at 50% 40%,rgba(245,158,11,0.06),transparent 70%)}
.terminal-window{font-family:'JetBrains Mono','Fira Code',monospace}
.main-card{
    background:linear-gradient(135deg,rgba(18,18,32,0.98),rgba(28,28,50,0.95));
    border:1px solid rgba(255,255,255,0.1);
    box-shadow:0 25px 80px rgba(0,0,0,0.6),0 0 60px rgba(245,158,11,0.04),inset 0 1px 0 rgba(255,255,255,0.06);
    animation:border-glow 6s ease-in-out infinite;
}
.main-card::before{content:'';position:absolute;inset:0;border-radius:inherit;background:linear-gradient(135deg,rgba(245,158,11,0.03),transparent 40%,transparent 60%,rgba(59,130,246,0.02));pointer-events:none}
.glass-inner{background:rgba(255,255,255,0.01);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.input-field{background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);transition:all .3s cubic-bezier(.4,0,.2,1)}
.input-field:focus{background:rgba(255,255,255,0.09);border-color:rgba(245,158,11,0.5);box-shadow:0 0 0 3px rgba(245,158,11,0.1),0 0 20px rgba(245,158,11,0.05)}
.btn-primary{background:linear-gradient(135deg,#f59e0b,#ea580c);transition:all .3s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden}
.btn-primary::before{content:'';position:absolute;top:0;left:-100%;width:100%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.2),transparent);transition:left .6s}
.btn-primary:hover::before{left:100%}
.btn-primary:hover{transform:translateY(-1px);box-shadow:0 8px 30px rgba(245,158,11,0.35)}
.btn-primary:active{transform:translateY(0)}
.particle{position:absolute;border-radius:50%;pointer-events:none}
.divider-v{width:1px;background:linear-gradient(180deg,transparent 5%,rgba(255,255,255,0.06) 20%,rgba(245,158,11,0.12) 50%,rgba(255,255,255,0.06) 80%,transparent 95%)}
.stat-pill{background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.06);backdrop-filter:blur(8px)}
.grid-bg{background-image:linear-gradient(rgba(255,255,255,0.02) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,0.02) 1px,transparent 1px);background-size:32px 32px}
</style>
{% endblock %}

{% block body %}
<div class="page-bg min-h-screen flex items-center justify-center p-4 lg:p-8">
    <!-- Ambient particles -->
    <div class="particle float-1 w-72 h-72 blur-3xl" style="top:5%;left:10%;background:rgba(245,158,11,0.07)"></div>
    <div class="particle float-2 w-96 h-96 blur-3xl" style="top:40%;right:5%;background:rgba(59,130,246,0.05)"></div>
    <div class="particle float-3 w-56 h-56 blur-3xl" style="bottom:10%;left:30%;background:rgba(168,85,247,0.06)"></div>

    <!-- Main Card -->
    <div class="main-card relative rounded-3xl w-full max-w-[1100px] overflow-hidden fade-in">
        <div class="flex flex-col lg:flex-row min-h-[600px]">

            <!-- LEFT COL: Brand + Terminal -->
            <div class="lg:w-1/2 relative p-8 lg:p-10 flex flex-col justify-between overflow-hidden">
                <!-- Grid background -->
                <div class="absolute inset-0 grid-bg opacity-50"></div>
                <!-- Corner accent -->
                <div class="absolute top-0 left-0 w-32 h-32 rounded-br-full" style="background:linear-gradient(135deg,rgba(245,158,11,0.1),transparent)"></div>

                <!-- Brand -->
                <div class="relative z-10 fade-in fade-d1">
                    <div class="flex items-center gap-3">
                        <div class="w-9 h-9 rounded-xl bg-gradient-to-br from-amber-500 to-orange-600 flex items-center justify-center pulse-glow">
                            <svg class="w-4.5 h-4.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/></svg>
                        </div>
                        <span class="text-lg font-bold text-white tracking-tight">SynavueDev</span>
                    </div>
                </div>

                <!-- Hero -->
                <div class="relative z-10 flex-1 flex flex-col justify-center py-6">
                    <h2 class="text-3xl lg:text-4xl font-bold text-white leading-tight mb-3 fade-in fade-d2">
                        Build. Ship.<br>
                        <span class="bg-gradient-to-r from-amber-400 via-orange-400 to-amber-500 bg-clip-text text-transparent">Measure.</span>
                    </h2>
                    <p class="text-gray-400 text-sm leading-relaxed mb-6 fade-in fade-d2 max-w-sm">
                        Your command center for engineering excellence. Track projects, sprints, and delivery velocity.
                    </p>

                    <!-- Terminal -->
                    <div class="terminal-window rounded-xl overflow-hidden bg-black fade-in fade-d3" style="border:1px solid rgba(255,255,255,0.08)">
                        <div class="flex items-center gap-2 px-3.5 py-2.5" style="border-bottom:1px solid rgba(255,255,255,0.05);background:rgba(255,255,255,0.03)">
                            <div class="flex gap-1.5">
                                <div class="w-2.5 h-2.5 rounded-full bg-[#ff5f57]"></div>
                                <div class="w-2.5 h-2.5 rounded-full bg-[#febc2e]"></div>
                                <div class="w-2.5 h-2.5 rounded-full bg-[#28c840]"></div>
                            </div>
                            <span class="text-[10px] text-gray-600 ml-1.5">~/projects</span>
                        </div>
                        <div class="p-4 text-[12px] leading-relaxed space-y-1.5">
                            <div class="flex gap-2"><span class="text-emerald-400">❯</span><span class="text-gray-300" id="t1"></span></div>
                            <div class="text-gray-600 text-[11px]" id="t2" style="display:none">✓ 3 projects loaded</div>
                            <div class="flex gap-2 mt-2" id="t3" style="display:none"><span class="text-emerald-400">❯</span><span class="text-gray-300"></span></div>
                            <div id="t4" style="display:none" class="ml-3 space-y-0.5 text-[11px]">
                                <div class="text-amber-500/70">┌─────────────────────────────────┐</div>
                                <div><span class="text-white/20">│</span> <span class="text-blue-400">Project-A</span>    <span class="text-emerald-400">● active</span>  <span class="text-gray-600">12 tasks</span> <span class="text-white/20">│</span></div>
                                <div><span class="text-white/20">│</span> <span class="text-blue-400">Project-B</span>    <span class="text-amber-400">◐ sprint</span>  <span class="text-gray-600"> 8 tasks</span> <span class="text-white/20">│</span></div>
                                <div><span class="text-white/20">│</span> <span class="text-blue-400">Project-C</span>    <span class="text-emerald-400">● active</span>  <span class="text-gray-600"> 5 tasks</span> <span class="text-white/20">│</span></div>
                                <div class="text-amber-500/70">└─────────────────────────────────┘</div>
                            </div>
                            <div class="flex gap-2 mt-2" id="t5" style="display:none"><span class="text-emerald-400">❯</span><span class="text-gray-300"></span></div>
                            <div id="t6" style="display:none" class="ml-3 text-[11px]">
                                <span class="text-emerald-400">↑ 42pts/sprint</span>
                                <span class="text-gray-700 mx-1">·</span>
                                <span class="text-blue-400">94% on-time</span>
                                <span class="text-gray-700 mx-1">·</span>
                                <span class="text-purple-400">3 PRs today</span>
                            </div>
                            <div class="flex gap-2 mt-2" id="t7" style="display:none">
                                <span class="text-emerald-400">❯</span>
                                <span class="text-gray-600 border-r-2 border-emerald-400/70 pr-0.5" style="animation:blink 1s step-end infinite">_</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Stats -->
                <div class="relative z-10 flex gap-3 fade-in fade-d4">
                    <div class="stat-pill rounded-lg px-4 py-2.5 flex-1 text-center">
                        <p class="text-lg font-bold text-white">99.9%</p>
                        <p class="text-[9px] text-gray-500 uppercase tracking-widest">Uptime</p>
                    </div>
                    <div class="stat-pill rounded-lg px-4 py-2.5 flex-1 text-center">
                        <p class="text-lg font-bold text-white">10x</p>
                        <p class="text-[9px] text-gray-500 uppercase tracking-widest">Delivery</p>
                    </div>
                    <div class="stat-pill rounded-lg px-4 py-2.5 flex-1 text-center">
                        <p class="text-lg font-bold text-white">∞</p>
                        <p class="text-[9px] text-gray-500 uppercase tracking-widest">Scale</p>
                    </div>
                </div>
            </div>

            <!-- DIVIDER -->
            <div class="hidden lg:block divider-v my-8"></div>

            <!-- RIGHT COL: Login Form -->
            <div class="lg:w-1/2 p-8 lg:p-10 flex flex-col justify-center relative">
                <!-- Corner accent -->
                <div class="absolute bottom-0 right-0 w-40 h-40 rounded-tl-full" style="background:linear-gradient(315deg,rgba(245,158,11,0.06),transparent)"></div>

                <div class="relative z-10 w-full max-w-[380px] mx-auto">
                    <!-- Mobile brand -->
                    <div class="lg:hidden text-center mb-8 fade-in">
                        <div class="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-gradient-to-br from-amber-500 to-orange-600 mb-2 pulse-glow">
                            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/></svg>
                        </div>
                        <h1 class="text-xl font-bold text-white">SynavueDev</h1>
                    </div>

                    <div class="mb-7 fade-in fade-d1">
                        <h2 class="text-xl font-bold text-white mb-1">Welcome back</h2>
                        <p class="text-gray-500 text-sm">Sign in to your workspace</p>
                    </div>

                    <form id="loginForm" class="space-y-4 fade-in fade-d2">
                        <div>
                            <label class="block text-[10px] font-semibold text-gray-400 uppercase tracking-widest mb-1.5">Username or Email</label>
                            <div class="relative">
                                <div class="absolute left-3.5 top-1/2 -translate-y-1/2 text-gray-500">
                                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
                                </div>
                                <input type="text" id="username" required autocomplete="username" class="input-field w-full pl-10 pr-4 py-3 rounded-xl text-white text-sm placeholder-gray-600 focus:outline-none" placeholder="Username or email">
                            </div>
                        </div>
                        <div>
                            <label class="block text-[10px] font-semibold text-gray-400 uppercase tracking-widest mb-1.5">Password</label>
                            <div class="relative">
                                <div class="absolute left-3.5 top-1/2 -translate-y-1/2 text-gray-500">
                                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg>
                                </div>
                                <input type="password" id="password" required autocomplete="current-password" class="input-field w-full pl-10 pr-11 py-3 rounded-xl text-white text-sm placeholder-gray-600 focus:outline-none" placeholder="Enter your password">
                                <button type="button" onclick="togglePassword()" class="absolute right-3.5 top-1/2 -translate-y-1/2 text-gray-500 hover:text-gray-300 transition">
                                    <svg id="eyeIcon" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                                </button>
                            </div>
                        </div>
                        <div id="loginError" class="hidden text-red-400 text-sm bg-red-500/10 border border-red-500/20 rounded-xl p-3 flex items-center gap-2">
                            <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L4.082 16.5c-.77.833.192 2.5 1.732 2.5z"/></svg>
                            <span id="loginErrorText"></span>
                        </div>
                        <button type="submit" id="loginBtn" class="btn-primary w-full py-3 text-white font-semibold rounded-xl text-sm tracking-wide flex items-center justify-center gap-2">
                            <span id="loginBtnText">Sign In</span>
                            <svg id="loginBtnArrow" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6"/></svg>
                            <svg id="loginBtnSpinner" class="w-4 h-4 animate-spin hidden" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"></path></svg>
                        </button>
                    </form>

                    <div class="mt-8 pt-6 fade-in fade-d3" style="border-top:1px solid rgba(255,255,255,0.06)">
                        <div class="flex items-center justify-center gap-4 text-[10px] text-gray-600">
                            <span class="flex items-center gap-1"><svg class="w-3 h-3 text-emerald-500/50" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>256-bit encrypted</span>
                            <span class="text-gray-700">·</span>
                            <span>SOC 2 compliant</span>
                            <span class="text-gray-700">·</span>
                            <span>Zero-trust</span>
                        </div>
                        <p class="text-center text-[10px] text-gray-700 mt-3">Synavue Technologies &copy; 2026</p>
                    </div>
                </div>
            </div>

        </div>
    </div>
</div>

{% endblock %}

{% block scripts %}
<script>
function togglePassword(){const p=document.getElementById('password');p.type=p.type==='password'?'text':'password';}

// Terminal typing animation
(function(){
    const cmds=[
        {el:'t1',text:'synavuedev projects --list',delay:0},
        {el:'t2',show:true,delay:1200},
        {el:'t3',text:'synavuedev board --status',delay:1800,child:'span:last-child'},
        {el:'t4',show:true,delay:2800},
        {el:'t5',text:'synavuedev metrics --sprint current',delay:3800,child:'span:last-child'},
        {el:'t6',show:true,delay:4800},
        {el:'t7',show:true,delay:5500},
    ];
    cmds.forEach(c=>{setTimeout(()=>{const el=document.getElementById(c.el);if(!el)return;if(c.show){el.style.display='';return;}const t=c.child?el.querySelector(c.child):el.querySelector('span:last-child');if(!t)return;el.style.display='';let i=0;const iv=setInterval(()=>{if(i<=c.text.length){t.textContent=c.text.slice(0,i);i++;}else clearInterval(iv);},35);},c.delay);});
})();

// Login handler
document.getElementById('loginForm').addEventListener('submit',async(e)=>{
    e.preventDefault();
    const btn=document.getElementById('loginBtn'),err=document.getElementById('loginError');
    document.getElementById('loginBtnText').textContent='Signing in...';
    document.getElementById('loginBtnArrow').classList.add('hidden');
    document.getElementById('loginBtnSpinner').classList.remove('hidden');
    btn.disabled=true;err.classList.add('hidden');
    try{
        await API.login(document.getElementById('username').value,document.getElementById('password').value);
        document.getElementById('loginBtnText').textContent='Redirecting...';
        window.location.href='/dashboard';
    }catch(ex){
        document.getElementById('loginErrorText').textContent=ex.detail||'Authentication failed';
        err.classList.remove('hidden');
        document.getElementById('loginBtnText').textContent='Sign In';
        document.getElementById('loginBtnArrow').classList.remove('hidden');
        document.getElementById('loginBtnSpinner').classList.add('hidden');
        btn.disabled=false;
    }
});


if(API.getToken()) window.location.href='/dashboard';
</script>
{% endblock %}'''

path = os.path.join(TMPL, 'login.html')
with open(path, 'w') as f:
    f.write(login_html)
print(f"Written {len(login_html)} bytes to {path}")

