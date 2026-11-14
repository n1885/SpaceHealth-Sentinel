import streamlit as st 
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="SpaceHealth-Sentinel | NASA Space Apps" ,
    layout="wide"
)

# Header Section 
st.title("SpaceHealth-Sentinel")
st.markdown("### NASA / ESA Biological Risk Research & Countermeasure Analysis") 
st.markdown("___")


st.markdown("---")

# Verified quantitative evidence from published research 

st.divider()
st.header("Verified Quantitative Evidence")

evidence_dataset = st.selectbox(
    "Select Verified Dataset",
    [
        "ISS Bone Countermeasure Study",
        "NASA GenelLab GLDS-156"
        
    ],
    key="verified_dataset"
)

if evidence_dataset =="ISS Bone Countermeasure Study":
    bone_data = pd.DataFrame({
        "Countermeasure": [
            "Pre-ARED",
            "ARED",
            "ARED + Bisphosphonate"
        ],
        "Sample Size": [24, 20, 7],
        "Mean Mission Duration (days)": [172, 157, 164],
        "Mission Duration SD (days)": [28, 28, 15],
        "Lumbar Spine BMD Change (%)": [-4.4, -1.9, 2.8],
        "Trab becular Bone Score Change (%)": [-3.0, 0.2, -1.5]
    })

    st.subheader("ISS Bone Countermeasure Comparison")

    metric = st.radio(
        "Select Measurements",
        [
            "Lumbar Spine BMD Change (%)",
            "Trabecular Bone Score Change (%)"
        ],
        horizontal=True
    )

    fig = go.Figure()

    fig.add_trace(go.Bar(

    x=bone_data["Countermeasure"],
    text=bone_data[metric],
    textposition="outside",
    marker_color=["#38bdf8","#818cf8", "#34d399"]
    ))

    fig.add_hline(
    y=0,
    line_dash="dash",
    line_color="white"
)

    fig.update_layout(
    title="Published Group-Level Changes",
    yaxis_title=metric,
    xaxis_title="Countermeasure Group",
    template="plotly_dark",
    height=440
   )


    st.dataframe(
    bone_data,
    hide_index=True,
    use_container_width=True
   )

    st.info(
    """
    These are published group-level observations.
    They are not individual predictions or
    proof of casual superiority.
    """
   )

    st.link_button(
    "Read Original Bone Study",
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC12799719/"
   )



else:
    radiation_data = pd.DataFrame({
        "Radiation Dose (Gy)": [0, 2, 8],
        "Biological Samples": [7, 5, 6],
        "Sampling Time (hours)": [6, 6, 6]
    })

    st.subheader("Mouse Blood Radiation Experiment")

    fig =go.Figure()
    fig.add_trace(go.Bar(
        x=[f"{dose}Gy" for dose in radiation_data["Radiation Dose (Gy)"]],
        y=radiation_data["Biological Samples"],
        textposition="outside",
        marker_color=["#38bdf8", "#818cf8", "#34d399"]
    ))

    fig.add_hline(
        y=0,
        line_dash="dash",
        line_color="white"
    )

    fig.update_layout(
        title="Radiation Dose vs Biological Samples",
        xaxis_title="Radiation Dose (Gy)",
        yaxis_title="Biological Samples",
        template="plotly_dark",
        height=440
    )

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(
        radiation_data,
        hide_index=True,
        use_container_width=True
    )

    st.info(
        "Mouse blood was collected 6 hours after acute "
        "radiation exposure. This chart shows sample counts, "
        "not radiation-induced biological effect sizes."
    )

    st.link_button(
        "Open NASA GeneLab Dataset",
        "https://data.nasa.gov/dataset/identifying-radiation-exposure-biomarkers-from-mouse-blood-transcriptome"
        "identifying-radiation-exposure-biomarkers-from-mouse-blood-transcriptome"
    )

    st.caption(
        "Evidence provenance:published bone study and"
        "NASA GeneLab GLDS-156 metadata."
        "No syhnthetic measurements or extrapolated mission risks."
    )

st.divider()
st.header("Risk Prevention & Countermeasures")

methods = {
    "Bone Loss": ["Resistance Exercise", "ARED", "Bisphosphonates"],
    "Kidney Stones": ["Hydration", "Urine Chemistry Monitoring", "Dietary Strategies"],
    "Neurological Risks": ["Exercise", "Fluid Shift Research", "Monitoring"],
    "Radiation": ["Shielding", "Exposure Reduction", "Mission Planning"]
}

risk = st.selectbox("Select Biological Risk", list(methods))

st.subheader("Countermeasure Comparison")
st.table(pd.DataFrame({
    "Countermeasure": methods[risk],
    "Purpose": ["Risk reduction"] * len(methods[risk])
}))

st.info("Research-level comparison only. Effectiveness varies by study and evidence strenght.")

st.divider()
st.header("Evidence-Based Countermeasures")

countermeasures = {
    "Bone Loss": [
        ("ARED Resistance Exercise", "Mechanical loading", "ISS operational use", "May not fully protect trabecular bone"),
        ("ARED + Bisphosphonates", "Reduce bone resorption", "Human flight studies", "Medication risks; limited samples")
    ],
    "Kidney Stones": [
        ("Hydration", "Reduce urinary supersaturation", "NASA modeling and operational guidance", "Effect depends on fluid availability"),
        ("Potassium Citrate", "Modify urine chemistry", "Flight and ground research", "Requires clinical oversight")
    ],
    "Neurological Risks": [
        ("Lower Body Negative Preassure", "Modify headward fluid shifts", "Experimental", "SANS prevention not established"),
        ("Artificial Gravity", "Restore gravitational loading", "Experimental", "Limited flight validation")
    ],
    "Radiation": [
        ("Shielding", "Reduce radiation exposure", "Engineering and operational guidance", "Protection depends on radiation type"),
        ("Mission Planning", "Limit avoidable exposure", "NASA radiation standards", "Cannot elminate all exposure")
    ]
    
}

risk = st.selectbox("Select Risk", list(countermeasures))

df = pd.DataFrame(
    countermeasures[risk],
    columns=["Countermeasure", "Mechanism", "Evidence", "Limitation"]
)

st.subheader("Scientific Comparison")
st.dataframe(df, hide_index=True, use_container_width=True)

st.subheader("Research Interpretation")
for _, item in df.iterrows():
    with st.expander(item["Countermeasure"]):
        st.write("Mechanism:", item["Mechanism"])
        st.write("Evidence:", item["Evidence"])
        st.write("Limitation:", item["Limitation"])

st.caption("Qualitative research synthesis; not an efficacy ranking or individual medical advice.")

st.divider()
st.header("Kidney Stone Research")

kidney_data = pd.DataFrame({
    "Flight Phase": ["In-flight", "Post-flight (within 1 year)"],
    "High-Risk Group (%)": [20.8, 12.3]
})

fig = px.bar(
    kidney_data,
    x="Flight Phase",
    y="High-Risk Group (%)",
    color="Flight Phase",
    title="Calcium Oxalate Stone Risk Classification"
)

fig.update_yaxes(range=[0, 25])
st.plotly_chart(fig, use_container_width=True)

st.caption(
    "Model-based proportion with IRR > 1.2. "
    "Not an observed kidney stone incidence rate."
)

st.divider()
st.header("Urine Volume Changes During Spaceflight")

urine_data = pd.DataFrame({
    "Flight Phase": ["Pre-flight", "In-flight"],
    "Urine Volume (L/day)": [2.1, 1.6]
})

fig_urine = px.bar(
    urine_data,
    x="Flight Phase",
    y="Urine Volume (L/day)",
    color="Flight Phase",
    text="Urine Volume (L/day)",
    title="Urine Volume Before and During Spaceflight"
)

fig_urine.update_traces(textposition="outside")
fig_urine.update_yaxes(range=[0, 2.5])

st.plotly_chart(fig_urine, use_container_width=True)

st.caption(
    "Reported urine volume values from the research summary."
    "Original publication verification pending."
)

st.divider()
st.header("Bone-Kidney Connection")

calcium_data = pd.DataFrame({
    "Condition": [
        "In-flight",
        "Proposed Target"
    ],
    "Urinary Calcium (mg/day)": [241.5, 150]
})

fig_calcium = px.bar(
    calcium_data,
    x="Condition",
    y="Urinary Calcium (mg/day)",
    color="Condition",
    text="Urinary Calcium (mg/day)",
    title="Urinary Calcium Excretion Comparison"
)

fig_calcium.update_traces(textposition="outside")
fig_calcium.update_yaxes(range=[0, 300])

st.plotly_chart(fig_calcium, use_container_width=True)

st.caption(
    "241.5 mg/day is the reported in-flight value. "
    "150 mg/day represents a proposed threshold, not an observed outcome. "
    "Original publication verification pending. "
)

st.divider()
st.header("Countermeasure Scenario Analysis")

calcium_reduction = st.slider(
    "Modeled Calcium Reduction (mg/day)",
    min_value=45,
    max_value=49,
    value=47
)

baseline_calcium = 241.5
scenario_calcium = baseline_calcium - calcium_reduction

scenario_data =pd.DataFrame({
    "Scenario": ["In-flight Baseline", "Intervention Scenario"],
    "Urinary Calcium (mg/day)": [
        baseline_calcium,
        scenario_calcium
    ]
})

fig_scenario = px.bar(
    scenario_data,
    x="Scenario",
    y="Urinary Calcium (mg/day)",
    color="Scenario",
    text="Urinary Calcium (mg/day)",
    title="Urinary Calcium Countermeasure Comparison",
    color_discrete_sequence=["#E76F51", "#2A9D8F"]
)

fig_scenario.add_hline(
    y=150,
    line_dash="dash",
    line_color="orange",
    annotation_text="Proposed Target: <150 mg/day"
)

fig_scenario.update_traces(textposition="outside")
fig_scenario.update_yaxes(range=[0, 270])

st.plotly_chart(fig_scenario, use_container_width=True)

st.metric(
    "Scenario Calcium Excretion",
    f"{scenario_calcium:.1f} mg/day",
    delta=f"-{calcium_reduction} mg/day"
)

st.caption(
    "Source Goodenow et al., npj Microgravity (2022). "
    "Interactive arithmetic comparison using values from "
    "the research summary. This does not reproduce "
    "the publication's complete risk model."
)

st.markdown(
    "[Original Research](https://doi.org/10.1038/s41526-021-00187-z)"
)

st.divider()
st.header("Neuronal Protection - PROMETO 2")

st.subheader("Spaceflight-Incuded Neuronal Stress")

st.markdown("""
Spaceflight conditions, including microgravity and
space radiation, may disrupt neuronal redox homeostasis
and contribute to oxidative stress.

The PROMETEO 2 experiment investigated cerium oxide
nanoparticles (nanoceria) as a potential antioxidant
countermeasure in neuronal cell models.
""")

st.subheader("Investigated Protective Mechanisms")

st.info(
    "Nanoceria was investigated for its potential to"
    "modulative oxidative stress and support neuronal"
    "homeostasis under spaceflight conditions."
)

st.markdown(
    "[NASA OSDR research Portal]"
    "(https://osdr.nasa.gov/bio/repo/data/studies/OSD-1005)"
)

st.caption(
    "Source: PROMETEO 2 / NASA OSD-1005. "
    "Experimental research investigating the "
    "neuroprotective potential of nanoceria "
    "under spaceflight conditions."
)

st.subheader("Neuroprotection Mechanism")

fig_neuro = go.Figure()

steps = [
    "Spaceflight Conditions",
    "Oxidative Stress",
    "Neuronal Response",
    "Nanoceria Intervention"
]

fig_neuro.add_trace(go.Scatter(
    x=[1, 2, 3, 4],
    y=[1, 1, 1, 1],
    mode="lines+markers+text",
    textposition="top center", 
    marker=dict(size=24, color=[
        "#64748B", "#E76F51", "#F4A261", "#2A9D8F"
    ]),
    line=dict(color="#94A3B8", width=3),
    hoverinfo="text"
))
fig_neuro.update_layout(
    title="Spaceflight Stress and Investigated Neuroprotection",
    xaxis=dict(visible=False, range=[0.5, 4.5]),
    yaxis=dict(visible=False, range=[0.5, 1.5]),
    height=350,
    showlegend=False
)

st.plotly_chart(fig_neuro, use_container_width=True)

st.divider()
st.header("Scientific Sources & References")

st.markdown("""
### Kidney Stone Risk
Goodenow et al. (2022) - Spaceflight-associated
renal stone risk and countermeasure modeling.

[Original Research](https://doi.org/10.1038/s41526-021-00187-z)

### Bone Health
ISS Bone Countermeasure Study - Bone density
changes and countermeasure comparisons.

[Original Research](https://pmc.ncbi.nlm.nih.gov/articles/PMC12799719/)

### Neuronal Protection
PROMETEO 2 - Investigation of nanoceria
for neuronal protection in spaceflight.

[NASA OSDR Dataset](https://osdr.nasa.gov/bio/repo/data/studies/OSD-1005)

### Radiation Biology
NASA GeneLab GLDS-156 - Radiation exposure
and biological response research.

[NASA Dataset](https://data.nasa.gov/dataset/identifying-radiation-exposure-biomarkers-from-mouse-blood-transcriptome)
""")
st.caption(
    "Independent research visualization project based on "
    "published space biologu studies and public datasets. "
    "Not an official NASA or ESA application."
)
