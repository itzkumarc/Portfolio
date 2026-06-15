import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update Publications Section with full content and missing item
publications_new = """
            <!-- PUBLICATIONS SECTION -->
            <section id="publications" class="content-section">
                <div class="space-y-12">
                    <div>
                        <h2 class="font-display text-4xl font-extrabold text-primary dark:text-accent mb-2">Publications</h2>
                        <p class="text-outline dark:text-teal-400/70">Contributing to the scientific discourse in natural systems.</p>
                        <div class="w-20 h-1.5 bg-teal-500 rounded-full mt-4"></div>
                    </div>

                    <div class="space-y-6">
                        <!-- Pub 1 -->
                        <div class="p-8 bg-white border border-teal-50 rounded-[40px] hover:shadow-xl transition-all dark:bg-[#001f1c] dark:border-teal-900">
                            <span class="text-[10px] font-bold text-teal-600 uppercase tracking-widest dark:text-teal-400">Int. J. of Agriculture Sciences</span>
                            <h4 class="text-2xl font-bold text-primary mt-2 dark:text-teal-100 leading-tight">Statistical evaluation of growth models for area, production, and productivity of tapioca</h4>
                            <p class="mt-4 text-sm text-outline dark:text-teal-100/70 italic">"Evaluation of nonlinear growth models for estimating biomass yield in tapioca cultivation systems under varying climatic conditions."</p>
                            <div class="flex gap-4 mt-6">
                                <a href="https://www.researchgate.net/publication/351123951" target="_blank" class="px-6 py-2 bg-primary text-white text-[10px] font-bold rounded-full dark:bg-teal-800 hover:bg-teal-700 transition-colors">READ PAPER</a>
                                <span class="px-4 py-2 border border-teal-100 text-[10px] font-bold text-teal-800 rounded-full dark:border-teal-800 dark:text-teal-300 uppercase tracking-widest">Growth Modeling</span>
                            </div>
                        </div>

                        <!-- Pub 2 -->
                        <div class="p-8 bg-white border border-teal-50 rounded-[40px] hover:shadow-xl transition-all dark:bg-[#001f1c] dark:border-teal-900">
                            <span class="text-[10px] font-bold text-teal-600 uppercase tracking-widest dark:text-teal-400">Aquaculture International</span>
                            <h4 class="text-2xl font-bold text-primary mt-2 dark:text-teal-100 leading-tight">Does abiotic stress influence the white fecal disease incidence and its intensity in Penaeus vannamei shrimp farms?</h4>
                            <p class="mt-4 text-sm text-outline dark:text-teal-100/70 italic">"Investigating the correlation between environmental abiotic factors and the prevalence of white fecal disease in P. vannamei through multivariate analysis."</p>
                            <div class="flex gap-4 mt-6">
                                <a href="https://www.researchgate.net/publication/389713821" target="_blank" class="px-6 py-2 bg-primary text-white text-[10px] font-bold rounded-full dark:bg-teal-800 hover:bg-teal-700 transition-colors">READ PAPER</a>
                                <span class="px-4 py-2 border border-teal-100 text-[10px] font-bold text-teal-800 rounded-full dark:border-teal-800 dark:text-teal-300 uppercase tracking-widest">Biostatistics</span>
                            </div>
                        </div>

                        <!-- Pub 3 -->
                        <div class="p-8 bg-white border border-teal-50 rounded-[40px] hover:shadow-xl transition-all dark:bg-[#001f1c] dark:border-teal-900">
                            <span class="text-[10px] font-bold text-teal-600 uppercase tracking-widest dark:text-teal-400">ResearchGate Publication</span>
                            <h4 class="text-2xl font-bold text-primary mt-2 dark:text-teal-100 leading-tight">Spatial and temporal variations of tapioca</h4>
                            <p class="mt-4 text-sm text-outline dark:text-teal-100/70 italic">"Analysis of spatial and temporal trends in tapioca production using GIS and statistical modeling."</p>
                            <div class="flex gap-4 mt-6">
                                <a href="https://www.researchgate.net/publication/372720320" target="_blank" class="px-6 py-2 bg-primary text-white text-[10px] font-bold rounded-full dark:bg-teal-800 hover:bg-teal-700 transition-colors">READ PAPER</a>
                                <span class="px-4 py-2 border border-teal-100 text-[10px] font-bold text-teal-800 rounded-full dark:border-teal-800 dark:text-teal-300 uppercase tracking-widest">GIS Analysis</span>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
"""

# Replace the publications section
content = re.sub(r'<!-- PUBLICATIONS SECTION -->.*?<section id="publications".*?</section>', publications_new, content, flags=re.DOTALL)

# 2. Update Conferences Section with full titles and remove duplicate tag
conferences_new = """
            <!-- CONFERENCES SECTION -->
            <section id="conferences" class="content-section">
                <div class="space-y-12">
                    <div>
                        <h2 class="font-display text-4xl font-extrabold text-primary dark:text-accent mb-2">Conferences</h2>
                        <p class="text-outline dark:text-teal-400/70">Sharing research insights at global symposia.</p>
                        <div class="w-20 h-1.5 bg-teal-500 rounded-full mt-4"></div>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="p-8 bg-white border border-teal-50 rounded-[40px] dark:bg-[#001f1c] dark:border-teal-900">
                            <div class="flex justify-between items-start mb-4">
                                <div class="w-12 h-12 bg-teal-50 rounded-2xl flex items-center justify-center dark:bg-teal-950">
                                    <span class="material-symbols-outlined text-teal-600">groups</span>
                                </div>
                                <span class="text-[10px] font-bold text-teal-600 dark:text-teal-400">SEP 2024</span>
                            </div>
                            <h4 class="text-lg font-bold text-primary dark:text-teal-100 leading-tight">12th Symposium on Diseases in Asian Aquaculture</h4>
                            <p class="text-xs text-outline mt-2 dark:text-teal-400/70">Bangkok, Thailand</p>
                            <p class="mt-4 text-sm text-outline dark:text-teal-100/70 leading-relaxed">Presented: "A machine learning approach for shrimp diseases prediction using culture and climatic parameters".</p>
                        </div>

                        <div class="p-8 bg-white border border-teal-50 rounded-[40px] dark:bg-[#001f1c] dark:border-teal-900">
                            <div class="flex justify-between items-start mb-4">
                                <div class="w-12 h-12 bg-teal-50 rounded-2xl flex items-center justify-center dark:bg-teal-950">
                                    <span class="material-symbols-outlined text-teal-600">analytics</span>
                                </div>
                                <span class="text-[10px] font-bold text-teal-600 dark:text-teal-400">AUG 2023</span>
                            </div>
                            <h4 class="text-lg font-bold text-primary dark:text-teal-100 leading-tight">Emerging Trends in Statistics and Data Science</h4>
                            <p class="text-xs text-outline mt-2 dark:text-teal-400/70">Chennai, India</p>
                            <p class="mt-4 text-sm text-outline dark:text-teal-100/70 leading-relaxed">Presented: "Outlier Detection for Wholesale Price Index of Onion in India".</p>
                        </div>
                    </div>
                </div>
            </section>
"""

# Replace the conferences section (handling the potential duplicate tag)
content = re.sub(r'<!-- CONFERENCES SECTION -->.*?<section id="conferences".*?</section>', conferences_new, content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)

print("Content updated.")
